from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=10)
    highest=models.FloatField()
    lowest=models.FloatField()
    rank=models.IntegerField()


    def __str__(self):
        return self.name

