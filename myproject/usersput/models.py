from django.db import models

# Create your models here.
class cars(models.Model):
    model = models.CharField(max_length=32)
    price = models.PositiveIntegerField()