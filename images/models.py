from django.db import models
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

