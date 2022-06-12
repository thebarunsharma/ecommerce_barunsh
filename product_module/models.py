from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
