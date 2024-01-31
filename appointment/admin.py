from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from . import models
# Register your models here.
class AppoinmentAdminModel(admin.ModelAdmin):
    list_display =['patient_name','doctor_name','appointment_types','appointment_status','symptoms','time','cancel']
    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.last_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointment_types=="Online" and obj.appointment_status == "Running":
            email_subject = "Your online appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.patient.user , "doctor": obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            
    
admin.site.register(models.Appointment,AppoinmentAdminModel)