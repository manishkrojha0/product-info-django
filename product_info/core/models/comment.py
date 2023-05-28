from django.db import models

class Comment(models.Model):
    postId = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_comment")
    body = models.CharField(max_length=300)
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name="comment")
    
