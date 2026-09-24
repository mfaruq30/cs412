# restaurant/urls.py
# URL patterns for the restaurant app

from django.urls import path
from . import views

# URL patterns for this app:
urlpatterns = [
    path('', views.main, name='home'),                           # default page is the main page
    path('main', views.main, name='main'),                       # restaurant info page
    path('order', views.order, name='order'),                    # online order form
    path('confirmation', views.confirmation, name='confirmation'),  # processes the order
]
