from common.models import AutoTimestamp
from django.db import models
from django.utils import timezone

# Create your models here.

class Picture(AutoTimestamp):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(blank=True, null=True)
    uploaded_by = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.approved and not self.approved_at:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)
