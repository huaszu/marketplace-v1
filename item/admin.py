from django.contrib import admin

# Register your models here.
from .models import Category, Item

# To get database table to show in Django administration interface
admin.site.register(Category)
admin.site.register(Item)