from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self) -> None:
        self.data = Category.objects.create(name='fun', slug='fun')
    
    def test_category(self):
        testCategory = self.data
        self.assertTrue(isinstance(testCategory, Category))
        self.assertEqual(str(testCategory), 'fun')
        
             

class ProductTest(TestCase): 
    def setUp(self) -> None:
        category = Category.objects.create(name='fun', slug='fun')
        user = User.objects.create(username='admin')
        self.data = Product.products.create(title='booktest',slug='fun',
                                           category=category,created_by=user, 
                                           image='test.png',price='50.01')   
        
    def test_product(self):
        testProduct = self.data
        self.assertTrue(isinstance(testProduct, Product))
        self.assertEqual(str(testProduct), 'booktest')
        
    

