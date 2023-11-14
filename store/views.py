from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *

# Create your views here.
# categories functions
def allCategories(request):
    categories = Category.getAllCategories()
    return {
        'categories': categories
    }
    
def listCategories(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    booksByCategory = Product.objects.filter(category=category)
    return render(request, 'store/search.html',{'books': booksByCategory,
                                                'category': category })


# Products function
def allBooks(request):
    books = Product.getAllProducts()
    return render(request, 'store/index.html', {'books': books})


def getBook(request, slug):
    book = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/detail.html', {'book': book})
    

