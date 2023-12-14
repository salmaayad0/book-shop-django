"""
cart class to provid defult behavior to cart sessions
"""

class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
    def add_to_cart(self, product):
        product_id = product.id
        
        if product_id not in self.cart:
            self.cart[product_id] = {'price' : product.price}  
              
        self.session.modified = True
        
        
    
    