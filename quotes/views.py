from django.shortcuts import render
import random
# Create your views here.
quotes = [
    "If Your Dreams Don't Scare You, Your Dreams Aren't Big Enough",
    "Float Like a Buttefly, Sting Like a Bee",
    "Impossible is just a big word thrown around by small men",
]

images = [
    "https://commons.wikimedia.org/wiki/Special:FilePath/Muhammad_Ali_NYWTS.jpg",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Muhammad_Ali_1963.jpg",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Muhammad_Ali_1966.jpg",
]

def quote(request):
    context = {
        'quote': random.choice(quotes),
        'image': random.choice(images),
    }
    return render(request, 'quotes/quote.html', context)

def show_all(request):
    context = {
        'quotes': quotes,

        'images': images, }

    return render(request, 'quotes/show_all.html', context)

def about(request):
    
    return render(request,  'quotes/about.html')