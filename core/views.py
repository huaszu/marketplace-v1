from django.shortcuts import render

from item.models import Category, Item

from .forms import SignupForm

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

def signup(request):
    # Create instance of form
    form = SignupForm

    return render(request, 'core/signup.html', {
        'form': form
    })