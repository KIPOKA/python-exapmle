from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name} is {self.age} years old'
