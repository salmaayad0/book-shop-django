"""
cart class to provid defult behavior to cart sessions
"""

class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('skey')
        
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
            
        self.cart = cart
        
        
    def add_to_cart(self, product, qty):
        product_id = str(product.id)

        if product_id not in self.cart:
             self.cart[product_id] = {}
             
        self.cart[product_id]['qty'] = qty
        self.cart[product_id]['price'] = str(product.price)
        
        self.session.modified = True
        

    
    
    
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
        
        
    
    