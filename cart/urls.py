from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('items', order_items, name='order_items'),
    path('submit/', order_submit, name='order_submit'),
]
