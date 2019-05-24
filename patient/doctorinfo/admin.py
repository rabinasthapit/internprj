from django.contrib import admin

# Register your models here.
from .models import DoctorProfile,Department,Services,PatientList
admin.site.register(DoctorProfile)
admin.site.register(Department)
admin.site.register(Services)
admin.site.register(PatientList)
