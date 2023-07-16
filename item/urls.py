from django.urls import path

from . import views

app_name = 'item' # namespace for this app

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]