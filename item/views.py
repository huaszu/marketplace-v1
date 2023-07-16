from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item
from .forms import NewItemForm, EditItemForm

def detail(request, pk):
    # 404 if object does not exist in db
    # `pk=pk`: First pk is primary key in db.  Second pk is from URL
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

# Django helps us make sure only logged in user can make a new item.  If not logged in, user is redirected to login page
@login_required
def new(request):
    if request.method == 'POST':
        # Make sure we get file that user uploads
        form = NewItemForm(request.POST, request.FILES)
        # Note: In /item/templates/item/form.html, `enctype="multipart/form-data">` facilitates image upload

        if form.is_valid():
            # `commit = False` to avoid db error because `created_by` field not yet present
            # Only create object but not save in db
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else: # If request is GET request
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item', 
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else: # If request is GET request
        # form = EditItemForm() # Form would be blank
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item', 
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')