from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = ("Categories")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})



class Product(models.Model):
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/store/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_by')
    
    class Meta:
        ordering = ['-created_time']
    
    def __str__(self):
        return self.title