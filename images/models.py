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
