"""
    Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', allBooks, name='allBooks'),
    path('<slug:slug>', getBook, name='getBook'),
    path('search/<slug:slug_category>', listCategories, name='listCategories'),
]
