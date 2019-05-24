from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'doctordashboard/$',views.doctordashboard,name='doctordashboard'),
    url(r'doctordashboard/patientlist/$',views.patientlist,name='patientlist'),
    url(r'doctordashboard/approve/',views.approve_appointment,name='approve_appointment'),
    url(r'doctordashboard/pat_delete/(?P<id>[0-9]+)/$',views.pat_delete,name='pat_delete'),
    url(r'doctordashboard/appointments/',views.appointments,name='appointments'),
    url(r'doctordashboard/appointment_delete/(?P<id>[0-9]+)/$',views.appointment_delete,name='appointmentdelete'),
    url(r'doctordashboard/send_report',views.send_report,name='send_report'),
    url(r'patientdashboard/$',views.patientdashboard,name='patientdashboard'),
    url(r'patientdashboard/makeappointment',views.makeappointment,name='makeappointment'),
    url(r'patientdashboard/report',views.report,name='report'),
    url(r'patientdashboard/editprofile/',views.editprofile,name='editprofile'),
    url(r'^logout/',auth_view.logout,{'next_page':'/myaccount/user_login'},name='logout'),
]
