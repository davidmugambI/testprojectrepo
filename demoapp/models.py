from django.db import models

# Create your models here.
class demotable(models.Model):
    firstname = models.CharField(max_length=12)
    image = models.ImageField(upload_to='photos')
    gender = models.CharField(max_length=8)