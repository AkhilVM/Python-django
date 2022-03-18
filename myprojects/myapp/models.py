from django.db import models

# Create your models here.

class place(models.Model):
    name= models.CharField(max_length = 250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250)
    descr = models.TextField()
