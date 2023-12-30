from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product

class TestCartView(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin')
        category = Category.objects.create(name='test', slug='test')
        Product.products.create(category=category, title='beginner', created_by=user,
                               slug='beginner', price='20.00', image='png')
        Product.products.create(category=category, title='intermediate', created_by=user,
                               slug='beginner', price='20.00', image='png')
        Product.products.create(category=category, title='advance', created_by=user,
                               slug='beginner', price='20.00', image='png')
        self.client.post(
            reverse('cart:order_submit'), {"bookId": 1, "bookQty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('cart:order_submit'), {"bookId": 2, "bookQty": 2, "action": "post"}, xhr=True)
        
        
        
    def test_cart_url(self):
        response = self.client.get(reverse('cart:order_items'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_cart_add(self):
        response = self.client.post(
            reverse('cart:order_submit'), {"bookId": 3, "bookQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('cart:order_submit'), {"bookId": 2, "bookQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})
        
        
    
    def test_cart_delete(self):
        response = self.client.post(
            reverse('cart:order_delete'), {"bookId": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 0, 'total_price': 0})
        
        
    def test_cart_update(self):
        response = self.client.post(
            reverse('cart:order_update'), {"bookId": 2, "bookQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 0, 'total_price': 0})
    
