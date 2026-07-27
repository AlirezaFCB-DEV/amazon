from django.db import models

class Category(models.Model) :
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255 , unique=True)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey("self" , on_delete=models.PROTECT , null=True , blank=True , related_name="children")
    
    class Meta :
        indexes = [
            models.Index(fields=["slug"])
        ]
        
class Brand(models.Model) :
    name = models.CharField(max_length=255 , unique=True)
    logo = models.ImageField(upload_to="images/")
    description = models.TextField()
    
class ProductColor(models.Model) :
    color = models.CharField(max_length=10)
    added_price = models.PositiveIntegerField()
    
class ProductSize(models.Model) :
    size = models.CharField(max_length=10)
    added_price = models.PositiveIntegerField()
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255 , unique=True) 
    category = models.ForeignKey(Category , on_delete=models.PROTECT , related_name="products")
    color = models.ForeignKey(ProductColor , on_delete=models.CASCADE , related_name="colors")
    size = models.ForeignKey(ProductSize , on_delete=models.CASCADE , related_name="sizes")
    
    
    brand = models.ForeignKey(Brand , on_delete=models.PROTECT , related_name="products")
    attributes = models.JSONField(default=dict , blank=True , db_index=True)
    stock = models.PositiveIntegerField(default=0)
    
    sku = models.CharField(max_length=15 , unique=True)
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - {self.price}"
