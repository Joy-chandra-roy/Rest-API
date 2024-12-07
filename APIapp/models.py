from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    dep=models.CharField(max_length=100)
    email=models.EmailField()
    phn=models.CharField(max_length=11)


    def __str__(self):
        return self.name
    