# restaurant/views.py
# view functions to handle URL requests for the restaurant app

from django.shortcuts import render, redirect
import random
import time

# regular menu items: form field name -> (item name, price)
menu = {
    'plov': ('Plov', 10.00),
    'samosa': ('Samosa', 9.00),
    'caesar_salad': ('Caesar Salad', 6.00),
}

# extras (options) that can be added to the plov: form value -> (extra name, price)
plov_extras = {
    'extra_chicken': ('Extra Chicken', 3.00),
    'extra_lamb': ('Extra Lamb', 4.00),
    'extra_beef': ('Extra Beef', 5.00),
}

# possible daily specials; one is chosen at random for the order page
daily_specials = [
    {'name': 'Thai Soup', 'description': 'Spicy coconut soup with lemongrass and herbs', 'price': 12.00},
    {'name': 'Duck', 'description': 'Roasted duck with seasonal vegetables', 'price': 22.00},
    {'name': 'Salmon Fillet', 'description': 'Pan-seared salmon with rice and greens', 'price': 20.00},
    {'name': 'Steak', 'description': 'Grilled steak with fries', 'price': 25.00},
]

# hours of operation shown on the main page: (day, hours)
hours = [
    ('Monday', '11:00 AM - 11:00 PM'),
    ('Tuesday', '11:00 AM - 11:00 PM'),
    ('Wednesday', '11:00 AM - 11:00 PM'),
    ('Thursday', '11:00 AM - 11:00 PM'),
    ('Friday', '11:00 AM - 11:00 PM'),
    ('Saturday', '11:00 AM - 11:00 PM'),
    ('Sunday', '11:00 AM - 11:00 PM'),
]


def main(request):
    '''Show the main page with basic information about the restaurant.'''

    template_name = 'restaurant/main.html'

    # create context variables for use in the template
    context = {
        'hours': hours,
    }

    return render(request, template_name, context)


def order(request):
    '''Show the online order form, including a randomly chosen daily special.'''

    template_name = 'restaurant/order.html'

    # create context variables for use in the template
    context = {
        'menu': menu,
        'plov_extras': plov_extras,
        'special': random.choice(daily_specials),  # pick today's special at random
    }

    return render(request, template_name, context)


def confirmation(request):
    '''Process the order form submission, and display a confirmation page.'''

    template_name = 'restaurant/confirmation.html'
    print(request.POST)

    # check if POST data was sent with the HTTP POST message:
    if request.POST:

        # extract customer info and special instructions into variables:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        instructions = request.POST['instructions']

        # build a list of (item name, price) for each item that was checked
        items = []
        total = 0

        for key in menu:
            if key in request.POST:
                item_name, price = menu[key]

                # add any extras the customer chose for the plov
                if key == 'plov':
                    for extra in request.POST.getlist('plov_extras'):
                        extra_name, extra_price = plov_extras[extra]
                        item_name += ' + ' + extra_name
                        price += extra_price

                items.append((item_name, price))
                total += price

        # the daily special: look up its price by name (don't trust prices from the form)
        if 'special' in request.POST:
            for special in daily_specials:
                if special['name'] == request.POST['special_name']:
                    items.append(('Daily Special: ' + special['name'], special['price']))
                    total += special['price']

        # ready time is a random number of minutes (30-60) from now
        ready_seconds = time.time() + random.randint(30, 60) * 60
        readytime = time.strftime('%A %I:%M %p', time.localtime(ready_seconds))

        # create context variables for use in the template
        context = {
            'items': items,
            'total': total,
            'name': name,
            'phone': phone,
            'email': email,
            'instructions': instructions,
            'readytime': readytime,
        }

        # delegate the response to the template, provide context variables
        return render(request, template_name=template_name, context=context)

    # default behavior: no form data (GET request), so send them to the order form
    return redirect('order')
