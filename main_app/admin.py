from django.contrib import admin
from .models import Cocktail, Preference, Ingredient

# Register your models here
admin.site.register(Cocktail)
admin.site.register(Preference)
admin.site.register(Ingredient)