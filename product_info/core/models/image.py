from django.db import models

class Image(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_url")
    url = models.URLField(null=True)