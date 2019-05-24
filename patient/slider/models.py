from django.db import models
# Create your models here.

class Slider(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='slider/')
    title=models.CharField(max_length=50,default=1)
    description=models.CharField(max_length=100,default=1)

    def __str__(self):
        return self.name
