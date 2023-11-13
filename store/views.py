from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
# categories functions

def allCategories(request):
    categories = Category.getAllCategories()
    return {
        'categories': categories
    }

# Products function
def allBooks(request):
    books = Product.getAllProducts()
    return render(request, 'store/index.html', {'books': books})


def getBook(request, slug):
    book = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/detail.html', {'book':book})
    

