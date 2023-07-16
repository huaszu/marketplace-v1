from django.shortcuts import render, get_object_or_404

from .models import Item

def detail(request, pk):
    # 404 if object does not exist in db
    # `pk=pk`: First pk is primary key in db.  Second pk is from URL
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })