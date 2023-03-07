from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'food'
        