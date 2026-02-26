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
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    attributes = models.JSONField(default=dict , blank=True , db_index=True)
    price = models.DecimalField(max_digits=12 , decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    
    