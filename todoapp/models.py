from django.db import models

# Create your models here.
class Task(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=250)
    priority=models.IntegerField()

    def __str__(self):
        return self.name