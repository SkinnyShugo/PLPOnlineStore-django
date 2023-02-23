from django.db import models
from django.urls import reverse
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
#from django.template.defaultfilters import slugify
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = RichTextUploadingField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        
    def __str__(self):
        return self.name

    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    

class Cart(models.Model):
    cart_id = models.CharField(max_length=355, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    token = models.CharField(max_length=20, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ZAR Order Total')
    emailAddress = models.EmailField(max_length=200, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=30, blank=True)
    billingAddress1 = models.CharField(max_length=30, blank=True)
    billingCity = models.CharField(max_length=30, blank=True)
    billingPostalCode = models.CharField(max_length=30, blank=True)
    billingCountry = models.CharField(max_length=30, blank=True)
    shippingName = models.CharField(max_length=30, blank=True)
    shippingAddress1 = models.CharField(max_length=30, blank=True)
    shippingCity = models.CharField(max_length=30, blank=True)
    shippingPostalCode = models.CharField(max_length=30, blank=True)
    shippingCountry = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ZAR price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product