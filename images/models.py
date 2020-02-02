from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    image_name = models.charField(max_length=40)
    image_description = models.charField(max_length=300)
