from django.db import models

# Create your models here.

class Course(models.Model):
   
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'courses'
    

class Student(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)  
    sName = models.CharField(max_length=100)
    sRollno = models.IntegerField()
    sEmail = models.EmailField()
    sPassword = models.CharField(max_length=100)
    sAge = models.PositiveIntegerField()
    sCollege = models.CharField(max_length=100)
    sStatus = models.BooleanField(default=True)
    sTermDate = models.DateField()
    sResult = models.FloatField('percentage ')
    
    def __str__(self):
        return self.sName
    
    class Meta:
        db_table = 'students'

genderChoice = (("Male","male"),("Female","female"))
        
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(choices=genderChoice,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'facultys'
        
class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subjects'
        
class Batch(models.Model):
    
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE , null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'batchs'
    
    
