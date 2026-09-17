from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request):
    '''fund to respon to the "home" reqiest.'''

    response_text = '''
    
        <html>
        <h1>Hello, world!</h1>
        <html/>
    
    
    '''
    return HttpResponse(response_text)

def home_page(request):
    '''Response to the URL '', delegate work to a template.'''

    template_name = 'hw/home.html'
    return render(request, template_name)
