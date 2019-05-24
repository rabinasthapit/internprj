from django.shortcuts import render,redirect,HttpResponse
from myaccount.models import UserProfile
from django.contrib.auth import login
from django.contrib.auth import authenticate
from doctorinfo.models import DoctorProfile,PatientList
from patientinfo.models import PatientProfile,Medicine,MakeAppointment
# from django.contrib.auth import authenticate
from .forms import RegisterForm,LoginForm,MakeAppointmentForm,AddPatientForm,EditProfileForm,SendReportForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
# Create your views here.


def register(request):
    if request.method=='GET':
        context={
        'form':RegisterForm(),
        }
        return render(request,'register.html', context)

    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            if(request.POST.get('is_doctor')):
                doc = DoctorProfile()
                doc.fullname = request.POST.get('fullname')
                doc.contact=request.POST.get('contact')
                doc.address=request.POST.get('address')
                doc.image=request.POST.get('image')
                doc.save()

            elif(request.POST.get('is_patient')):
                pat=PatientProfile()
                pat.fullname=request.POST.get('fullname')   # agadi ko fullname model bata
                pat.address=request.POST.get('address')
                pat.contact=request.POST.get('contact')
                pat.image=request.POST.get('image')

                pat.save()

            form.save()
            return redirect('user_login')

        else:
            return render(request,'register.html',{'form':form,'errmsg':'Password didnt match'})



def user_login(request):
    if request.method=='GET':
        context={
        'form' :LoginForm(),
        }
        return render(request,'login.html',context)

    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=authenticate(email=email,password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('dashboard')
            else:
                return render(request,'login.html',{'errmsg':'no users found'})
        else:
            return render(request,'login.html',{'errmsg':'something went wrong2'})




def dashboard(request):
    if not request.user.is_authenticated():
        return redirect('user_login')
    else:
        if request.method=='GET':
            login_user_id=request.user.id

            user=UserProfile.objects.get(id=login_user_id)
            if(user.is_doctor==True):
                return redirect('doctordashboard')

            else:
                return redirect('patientdashboard')

        else:
             return render(request,'test.html')


@login_required(login_url='myaccount/user_login/')
def doctordashboard(request):
    if request.method=='GET':
        context={
        'doc':UserProfile.objects.get(id=request.user.id)
        }
        return render(request,'doctordashboard.html',context)
    else:
        pass



@login_required(login_url='myaccount/user_login/')
def patientdashboard(request):
    if request.method=='GET':
        context={
        'pat':UserProfile.objects.get(id=request.user.id)
        }
        return render(request,'patientdashboard.html',context)
    else:
        pass





@login_required(login_url='myaccount/user_login/')
def patientlist(request):
    if request.method=='GET':
        context={
        'pat_list':PatientList.objects.all(),
        'form':AddPatientForm()
        }
        return render(request,'patientlist.html',context)
    else:
        form=AddPatientForm(request.POST)
        if form.is_valid():
            form.save();
            context={
            'pat_list':PatientList.objects.all(),
            'form':AddPatientForm()
            }
            return render(request,'patientlist.html',context)


@login_required(login_url='myaccount/user_login/')
def pat_delete(request,id):
    try:
        pat=PatientList.objects.get(id=id)
        pat.delete()
        return redirect('patientlist')

    except:
        return redirect('patientlist')


@login_required(login_url='myaccount/user_login/')
def makeappointment(request):
    if request.method=='GET':
        context={
        'form':MakeAppointmentForm()
        }
        return render(request,'makeappointment.html',context)
    else:
        form=MakeAppointmentForm(request.POST)
        if form.is_valid():
            make_appointment=form.save(commit=False)
            user=UserProfile.objects.get(id=request.user.id)
            make_appointment.user=user
            make_appointment.save()
            return redirect('patientdashboard')

        else:
            return render(request,'test.html')



@login_required(login_url='myaccount/user_login/')
def appointments(request):
    if request.method=='GET':
        context={
        'app_list':MakeAppointment.objects.all(),
        }
        return render(request,'appointments.html',context)
    else:
        pass


# apppointment_delete
@login_required(login_url='myaccount/user_login/')
def appointment_delete(request,id):
    try:
        pat=MakeAppointment.objects.get(id=id)
        pat.delete()
        return redirect('appointments')

    except:
        return redirect('appointments')


@login_required(login_url='myaccount/user_login/')
def report(request):
    if request.method=='GET':
        context={
        'pat_report':Medicine.objects.all()
        }
        return render(request,'report.html',context)
    else:
        pass


def editprofile(request):
    edit=UserProfile.objects.get(id=request.user.id)
    form=EditProfileForm(request.POST or None,instance=edit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context={
    'form':form
    }
    return render(request,'editprofile.html',context)

def approve_appointment(request):
    address=UserProfile.objects.get()
    email = EmailMessage('Hello', 'World', to=['user@gmail.com'])
    email.send()


def send_report(request):
    if request.method=='GET':
        context={
        'form':SendReportForm(),
        }
        return render(request,'sendreport.html',context)
    else:
        form=SendReportForm(request.POST)
        if form.is_valid():
            send_report=form.save(commit=False)
            user=UserProfile.objects.get(id=request.user.id)
            send_report.user=user
            send_report.save()
            return redirect('doctordashboard')

        else:
            return render(request,'test.html')
