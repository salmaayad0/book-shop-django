from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .cart import Cart
from store.models import Product

# Create your views here.
def order_items(request):
    return render(request, 'cart/items.html')


def order_submit(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookId'))
        book = get_object_or_404(Product, id=book_id)
        cart.add_to_cart(book)
        
        return JsonResponse({'test': 'data'})
