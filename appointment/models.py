from django.db import models
from doctor.models import Doctor,AvailableTime
from patient.models import Patient


# Create your models here.
APPOINTMENT_TYPES=[
    ('Online','Online'),
    ('Offline','Offline'),
]
APPOINTMENT_STATUS=[
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('Running','Running')
]
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_type=models.CharField(max_length=100,choices=APPOINTMENT_TYPES)
    appointment_status=models.CharField(max_length=100,choices=APPOINTMENT_STATUS ,default='Pending')
    appointment_date=models.ForeignKey(AvailableTime,on_delete= models.CASCADE)
    symptom=models.TextField()
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f'Doctor: {self.doctor.user.username} - Patient: {self.patient.user.username} '