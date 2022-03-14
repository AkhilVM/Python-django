from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    year = models.IntegerField()
    image1 = models.ImageField(upload_to="galary")
    image2 = models.ImageField(upload_to="galary")
    image3 = models.ImageField(upload_to="galary")

    def __str__(self):
        return self.name