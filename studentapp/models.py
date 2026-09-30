from django.db import models

# Create your models here.
class Student_detsils(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mark=models.IntegerField()
    cource=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    