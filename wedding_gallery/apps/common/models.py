from django.db import models

# Create your models here.

class AutoTimestamp(models.Model):
    id = models.UUIDField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True