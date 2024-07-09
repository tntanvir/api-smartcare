from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.
class Specialization(models.Model):
    name= models.CharField(max_length=30)
    slug= models.SlugField(max_length=40)
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    name= models.CharField(max_length=30)
    slug= models.SlugField(max_length=40)
    def __str__(self):
        return self.name
    
class AvailableTime(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='doctor/images/')
    designation= models.ManyToManyField(Designation)
    specialization=models.ManyToManyField(Specialization)
    available_time=models.ManyToManyField(AvailableTime)
    fee=models.IntegerField()
    meet_link=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} {self.user.last_name}'
    
STAR=[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    rating=models.CharField(choices=STAR,max_length=10)
    review_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'patient: {self.patient.user.first_name} - doctor: {self.doctor.user.first_name}'