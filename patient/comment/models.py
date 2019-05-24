from django.db import models
from doctorinfo.models import DoctorProfile

# Create your models here.
class Comment(models.Model):
    comments=models.CharField(max_length=200)
    date=models.DateField(max_length=10)
    doctor_id=models.ForeignKey(DoctorProfile,default=1)



    def __str__(self):
        return self.comments
