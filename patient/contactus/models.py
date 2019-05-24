from django.db import models
# from ckeditor.fields import RichTextField


# Create your models here.


class ContactUs(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=100)
    message=models.CharField(max_length=100)


    def __str__(self):
        return self.fullname

class CV(models.Model):
    name=models.CharField(max_length=100)
    cv_file=models.FileField(upload_to='cv/')

    def __str__(self):
        return self.name
