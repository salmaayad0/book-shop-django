from store.models import Product
from decimal import Decimal

class Cart():
    """
    cart class to provid defult behavior to cart sessions
    """
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('skey')
        
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
            
        self.cart = cart
    
    
    def __len__(self):
        return sum(product['qty'] for product in self.cart.values())
        
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart_copy = self.cart.copy()
        
        for product in products:
            cart_copy[str(product.id)]['product'] = product
            
        for item in cart_copy.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        
        
        
    def save(self):
        self.session.modified = True
        
        
        
    def add_to_cart(self, product, qty):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {}
             
        self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.save()
        
    
    
    def delete_from_cart(self, product_id):
        if str(product_id) in self.cart:
            print(self.cart[str(product_id)])
            del self.cart[str(product_id)]
            
            self.save()
    
    
    
    def update_cart(self, product_id, qty):
        if str(product_id) in self.cart:
            self.cart[str(product_id)]['qty'] = qty
            
            self.save()
    
    
    def get_total_price(self):
        return sum(Decimal(product['price']) * product['qty'] for product in self.cart.values())
    
    