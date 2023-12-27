from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
    
    @classmethod
    def getAllCategories(cls):
        return cls.objects.all()
    
    def getCategory_url(self):
        return reverse("store:listCategories", args=[self.slug])




class ProductManger(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(ProductManger, self).get_queryset().filter(is_active=True)

  

class Product(models.Model):
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True, 
                                   default='Nunc eget augue eu diam finibus dapibus quis sit amet leo. Ut gravida facilisis velit mollis fringilla. Quisque efficitur elit')
    image = models.ImageField(upload_to='images/store/', default='images/store/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_by')
    products=ProductManger()
    
    class Meta:
        ordering = ['-created_time']
    
    def __str__(self):
        return self.title
    

    def getAllProducts():
        return Product.products.all()
    
    # return one product url by slug
    def getOneProduct_url(self):
        return reverse('store:getBook', args=[self.slug])
    
    # return image url
    @property
    def getImage_url(self):
        return f'/media/{self.image}'
    