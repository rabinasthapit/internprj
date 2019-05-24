from django.db import models
from phone_field import PhoneField
# from comment.models import Comment
from doctorinfo.models import DoctorProfile
from myaccount.models import UserProfile
# Create your models here.

gender=(('m','Male'),('f','Female'))
class PatientProfile(models.Model):
    fullname=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=gender)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/')
    contact=models.CharField(max_length=100)
    doctorname=models.ForeignKey(DoctorProfile,default=1)
    user=models.ForeignKey(UserProfile,default=1)


    def __str__(self):
        return self.fullname


class MakeAppointment(models.Model):
    doctorname=models.CharField(max_length=100,default=1)
    symptom=models.TextField(max_length=1000)
    availabledate=models.CharField(max_length=100)
    availabletime=models.CharField(max_length=100)
    user=models.ForeignKey(UserProfile,default=1)

    def __str__(self):
        return self.doctorname



class Medicine(models.Model):
    medicine_name=models.CharField(max_length=100)
    start_date=models.CharField(max_length=50)
    dose=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(UserProfile,default=1)

    def __str__(self):
        return self.medicine_name
