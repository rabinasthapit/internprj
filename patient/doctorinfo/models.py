from django.db import models
from patient import settings
# from phone_field import PhoneField
from myaccount.models import UserProfile
# from ckeditor.fields import RichTextField
# Create your models here.

class Department(models.Model):
    departmentname=models.TextField(max_length=50)
    image=models.ImageField(upload_to='media/')
    description=models.TextField(max_length=1000)


    def __str__(self):
        return self.departmentname


class Services(models.Model):
    name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/')
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.name

gender=(('m','Male'),('f','Female'))
class DoctorProfile(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    date_of_birth=models.CharField(max_length=10,default=1)
    gender=models.CharField(max_length=10,choices=gender,default=1)
    contact=models.CharField(max_length=50)
    specialization=models.CharField(max_length=100)
    experience=models.CharField(max_length=100,default=1)
    image=models.ImageField(upload_to='media/')
    user=models.ForeignKey(UserProfile,default=1)

    def __str__(self):
        return self.fullname

class PatientList(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
