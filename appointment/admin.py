from django.contrib import admin
from .models import Appointment

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient','appointment_type','appointment_status','appointment_date','symptom','cancel']
    
    def doctor(self,obj):
        return obj.doctor.user.first_name
    def patient(self,obj):
        return obj.patient.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointment_status=='Running' and obj.appointment_type=='Online':
            email_subject='Appointment is Running'
            email_body=render_to_string('ap_running_email.html',{'user':obj.patient.user,'doctor':obj.doctor,'obj':obj})

            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(Appointment, AppointmentAdmin)
