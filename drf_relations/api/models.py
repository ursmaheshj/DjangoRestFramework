from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = [('Male','Male'),('Female','Female'),('Other','Other')]
    gender = models.CharField(max_length=10,choices=gender_choices,default='Male')

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=60)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    