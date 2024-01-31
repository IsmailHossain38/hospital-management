from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length =30)
    slug = models.SlugField(max_length =40)
    def __str__(self) -> str:
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length =30)
    slug = models.SlugField(max_length =40)
    def __str__(self) -> str:
        return self.name
    
class AvailableTime(models.Model):
    name= models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name
    
    
class Doctor(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models.ImageField(upload_to="doctor/image/")
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    availabletime = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link  = models.CharField(max_length =100)
    
    def __str__(self) -> str:
        return self.user.first_name
    
STARCHOICES =[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewers = models.ForeignKey(Patient ,on_delete =  models.CASCADE)
    doctor = models.ForeignKey(Doctor ,on_delete =  models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = STARCHOICES ,max_length =10)
    
    def __str__(self) -> str:
        return f"patient {self.reviewers.user.first_name} and Doctor {self.doctor.user.first_name}"