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
    
        
def order_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookId'))
        
        print(book_id)
        cart.delete_from_cart(product_id=book_id)
        qty = cart.__len__()
        total_price = cart.get_total_price()
        
        return JsonResponse({'qty': qty, 'total_price': total_price})
    

def order_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookId'))
        book_qty = int(request.POST.get('bookQty'))
        
        cart.update_cart(product_id=book_id, qty=book_qty)
        qty = cart.__len__()
        total_price = cart.get_total_price()
        
        return JsonResponse({'qty': qty, 'total_price': total_price})
        

