from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
# categories functions

def allCategories(request):
    categories = Category.getAllCategories()
    return {
        'categories': categories
    }

# Products function
def allProducts(request):
    products = Product.getAllProducts()
    return render(request, 'store/index.html', {'products': products})

def getProduct(request):
    return Product.getOneProduct_url