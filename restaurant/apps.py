# restaurant/apps.py
# app configuration for the restaurant app

from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    '''Configuration for the restaurant app.'''

    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant"
