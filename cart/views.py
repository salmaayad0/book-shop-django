from django.shortcuts import render

# Create your views here.
def order_items(request):
    return render(request, 'cart/items.html')
