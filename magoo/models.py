from django.db import models

# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=50)
    frequency = models.CharField(max_length=15)
    category = models.CharField(max_length=30)
    update_date = models.DateTimeField('Date Updated')