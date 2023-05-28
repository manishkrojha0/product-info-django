from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.TextField(max_length=300, null=False, default='')
    description = models.TextField(null=True, default='')
    price = models.IntegerField(null=True, default=0)
    discountPercentage = models.FloatField(null=True, default=0.0)
    rating = models.FloatField(null=True, default=0.0)
    stock = models.IntegerField(null=True, default=0)
    brand = models.CharField(max_length=250, null=False, default='')
    category = models.CharField(max_length=250, name=False, default='')
    thumbnail = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
    



