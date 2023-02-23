from django.db import models

# Create your models here.

#from mptt.fields import TreeForeignKey
#from mptt.models import MPTTModel
from django.urls import reverse
# Create your models here.

class Category(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.CharField(max_length=300, blank=True, null=True, unique=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_bycategory', args=[self.slug])
        
    def __str__(self):
        return self.name

    

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
"""
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '/'.join(full_path[::-1])
"""