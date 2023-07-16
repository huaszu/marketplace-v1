from django.shortcuts import render

from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    # Add context in curly braces
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items, # list of items that /core/templates/core/index.html loops through
    })

def contact(request):
    return render(request, 'core/contact.html')