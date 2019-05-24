from django.contrib import admin

# Register your models here.
from .models import ContactUs,CV
admin.site.register(ContactUs)
admin.site.register(CV)
