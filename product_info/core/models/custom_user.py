from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=300)