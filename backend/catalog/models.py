from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    attributes = models.JSONField(default=dict , blank=True)
    price = models.DecimalField(max_digits=12 , decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    
    