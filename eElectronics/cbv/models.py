from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'food'
    

class AddFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='upload/')    
    
    class Meta:
        db_table = 'addfile'
        