from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=60)
    passby = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name