from django.contrib import admin

from .models import PatientProfile,Medicine,MakeAppointment
# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(Medicine)
admin.site.register(MakeAppointment)
