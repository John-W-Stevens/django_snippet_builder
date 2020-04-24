from django.db import models

# Create your models here.
class ErrorMessage(models.Model):
    content = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
