from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from slider.models import Slider
from myaccount.forms import ContactForm,ApplyNowForm
from newsdetails.models import NewsDetails,VacancyDetails
from doctorinfo.models import Department,Services
from django.views.decorators.csrf import csrf_exempt
from myaccount.models import UserProfile

def home(request):
    context={
    'slider': Slider.objects.all()[0],
    'slider2': Slider.objects.all()[1:],
    's':Services.objects.all(),
    'd':Department.objects.all(),
    }
    return render(request,"index.html",context)


def aboutus(request):
    return render(request,'aboutus.html')



def contactus(request):
    if request.method=='GET':
        context={
        'form': ContactForm(),
        's':Services.objects.all(),
        'd':Department.objects.all(),
        }
        return render(request,'contactus.html',context)

    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contactus.html',{'form':ContactForm(),'msg':'Thank you for the message. We will get you back shortly!'})
        else:
            return render(request,'contactus.html',{'form':ContactForm()})

def news(request):
    context={
    'news':NewsDetails.objects.all(),
    'vacancy':VacancyDetails.objects.all(),
    's':Services.objects.all(),
    'd':Department.objects.all(),
    }
    return render(request,'news.html',context)

def newsdetails(request,id):
    context={
    'news':NewsDetails.objects.get(pk=id),
    's':Services.objects.all(),
    'd':Department.objects.all(),
    }
    return render(request,'newsdetails.html',context)


def vacancydetails(request,id):
    if request.method=='GET':
        context={
        'vacancy':VacancyDetails.objects.get(pk=id),
        'form':ApplyNowForm(),
        's':Services.objects.all(),
        'd':Department.objects.all(),
        }
        return render(request,'vacancydetails.html',context)
    else:
        pass
        # form=ApplyNowForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return render(request,'index.html',{'vacancy':VacancyDetails.objects.get(pk=id),})
        #
        # else:
        #     return render(request,'vacancydetails.html',{'errmsg':'Form not saved'})

@csrf_exempt
def vacancy_submit(request):
    vacancy_submit=ApplyNowForm(request.POST or None)
    if request.method=='POST' and request.is_ajax():
        print(request.POST.get('name'))
        print(request.FILES.get('cv_file'))
        if vacancy_submit.is_valid():
            vacancy_submit.save()
            msg="Updated"
        else:
            msg="not updated"
    else:
        msg="somethg went wrong"

    return HttpResponse(msg)


def department(request):
    context={
    'department':Department.objects.all(),
    's':Services.objects.all(),
    'd':Department.objects.all(),
    }
    return render(request,'department.html',context)



def departmentdetails(request,id):
    context={
    'department':Department.objects.get(pk=id),
    's':Services.objects.all(),
    'd':Department.objects.all(),

    }
    return render(request,'departmentdetails.html',context)


def services(request):
    context={
    'service':Services.objects.all(),
    's':Services.objects.all(),
    'd':Department.objects.all(),
    }
    return render(request,"services.html",context)

def servicedetails(request,id):
    context={
    'service':Services.objects.get(pk=id),
    's':Services.objects.all(),
    'd':Department.objects.all(),

    }
    return render(request,"servicedetails.html",context)

def search(request):
    if request.method=="POST":
        search_text=request.POST['search_text']
        search_text_length=len(search_text)
        if search_text_length >= 1:
            search_final_text=search_text
            print(search_final_text)
            search_results=UserProfile.objects.filter(fullname__contains=search_final_text)
            return render_to_response('ajax_search.html',{'results':search_results})
        print(search_text)

    else:
       search_text=" "
    return render_to_response('ajax_search.html',{})
