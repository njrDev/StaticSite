from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    disc = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    image = models.ImageField(upload_to='pics')
    person = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.person
