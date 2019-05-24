from django import forms
from django.forms import ModelForm,Form
from .models import UserProfile
from contactus.models import ContactUs,CV
from patientinfo.models import MakeAppointment,PatientProfile,Medicine
from doctorinfo.models import PatientList



class RegisterForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    def save(self,commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model=UserProfile
        exclude=('is_admin', 'is_medistore', 'is_active','is_lab','last_login','_is_staff')




class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=UserProfile
        fields=('email','password')



class ContactForm(ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'


class ApplyNowForm(ModelForm):
    class Meta:
        model=CV
        fields='__all__'


class MakeAppointmentForm(ModelForm):
    doc_choices=(('Dr. Sagun Maharjan','Dr. Sagun Maharjan'),('Dr. Sashil Maharjan','Dr.Sashil Maharjan'),('Dr. Susan','Dr. Susan'))
    doctorname=forms.CharField(widget=forms.Select(choices=doc_choices))
    availabledate=forms.CharField(max_length=100)
    availabletime=forms.CharField(max_length=100)

    class Meta:
        model=MakeAppointment
        fields=('doctorname','symptom','availabledate','availabletime')


class AddPatientForm(ModelForm):
    class Meta:
        model=PatientList
        fields=('fullname','contact','address')



class EditProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=('fullname','username','email', 'contact','address')


class SendReportForm(ModelForm):
    class Meta:
        model=Medicine
        exclude=('user',)
