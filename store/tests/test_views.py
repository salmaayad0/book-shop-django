from importlib import import_module
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth.models import User
from store.models import *
from store.views import allBooks


# Create your tests here.
class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        # as if these data created in database 'simulation'
        category = Category.objects.create(name='test', slug='test')
        user = User.objects.create(username='admin')
        product = Product.products.create(title='booktest',slug='booktest',
                                         category=category,created_by=user, 
                                           image='test.png',price='50.01') 
    
    
    # test allowed urls => if data needed use from above as it's no works as db
    def test_url_index(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_absolute_category(self):
        response = self.c.get(
            reverse("store:listCategories", args=["test"]))
        self.assertEqual(response.status_code, 200)
        
    def test_url_absolute_product(self):
        response = self.c.get(
            reverse('store:getBook', args=['booktest']))
        self.assertEqual(response.status_code, 200)
        
        
 
    def test_view_function(self):
        request = self.factory.get('/booktest')
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = allBooks(request)
        htmlPage = response.content.decode('utf8')
        self.assertIn('<title> Book Shop </title>', htmlPage)
        self.assertEqual(response.status_code, 200)
        
    
