from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.FloatField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

