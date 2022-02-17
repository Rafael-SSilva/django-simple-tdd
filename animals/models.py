from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=20)
    predator = models.CharField(max_length=5)
    venomous = models.CharField(max_length=5)
    domestic = models.CharField(max_length=5)

    def __str__(self):
        return self.name
