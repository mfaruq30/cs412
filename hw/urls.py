from django.urls import path
from django.conf import settings
from . import views

#Urls patterns to the hw app

urlpatterns = [
    # path(r'', views.home, name = "home"),
    path(r'', views.home_page, name = "home_page"),

]