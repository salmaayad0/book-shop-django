from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product

# Create your views here.
def order_items(request):
    cart=Cart(request)
    return render(request, 'cart/items.html', {'cart': cart})


def order_submit(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookId'))
        book_qty = int(request.POST.get('bookQty'))
        book = get_object_or_404(Product, id=book_id)
        cart.add_to_cart(product=book, qty=book_qty)
        total_qty = cart.__len__()
        
        return JsonResponse({'qty': total_qty})

