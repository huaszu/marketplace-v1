from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # iterable
        verbose_name_plural = 'Categories' # Otherwise, Django automatically writes 'Categorys'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    # If delete a category, all category's items also deleted
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # in case user does not provide description
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # Django creates folder 'item_images' if it does not already exist
    is_sold = models.BooleanField(default=False)
    # If delete a user, all user's items also deleted
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # index in db between this item and user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name