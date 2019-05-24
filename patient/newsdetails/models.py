from django.db import models

# Create your models here.


class NewsDetails(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media/')
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.title



class VacancyDetails(models.Model):
    vacancytitle=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.vacancytitle
