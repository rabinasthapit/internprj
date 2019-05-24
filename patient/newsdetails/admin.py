from django.contrib import admin

# Register your models here.
from .models import NewsDetails,VacancyDetails
admin.site.register(NewsDetails)
admin.site.register(VacancyDetails)
