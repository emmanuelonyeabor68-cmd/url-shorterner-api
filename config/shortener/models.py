from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField(max_length=1000)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code
