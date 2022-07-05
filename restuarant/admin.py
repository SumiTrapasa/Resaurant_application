from django.contrib import admin
from .models import Cuisines, Menu, Restuarant


# Register your models here.

admin.site.register(Restuarant)
admin.site.register(Cuisines)
admin.site.register(Menu)