"""patient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name='home'),
    url(r'^myaccount/',include('myaccount.urls')),
    url(r'^contactus/',views.contactus,name='contactus'),
    url(r'^aboutus/',views.aboutus,name='aboutus'),
    url(r'^news/$',views.news,name='news'),
    url(r'^news/newsdetails/(?P<id>[0-9]+)/$',views.newsdetails,name='newsdetails'),
    url(r'^news/vacancy/(?P<id>[0-9]+)/$',views.vacancydetails,name='vacancydetails'),
    url(r'^ajax/vacancy_submit/$',views.vacancy_submit,name='vacancy_submit'),
    # url(r'^news/vacancy/applynow/',views.applynow,name='applynow'),
    url(r'^department/$',views.department,name='department'),
    url(r'^department/departmentdetails/(?P<id>[0-9]+)/$',views.departmentdetails,name='departmentdetails'),
    url(r'^services/$',views.services,name='services'),
    url(r'^services/servicedetails/(?P<id>[0-9]+)/$',views.servicedetails,name='servicedetails'),
    url(r'^ajax/search/$',views.search,name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
