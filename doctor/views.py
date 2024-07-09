from django.shortcuts import render
from rest_framework import viewsets,filters
from .serializers import DesignationSerializer,SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer,DoctorSerializer
from .models import Specialization,Designation,AvailableTime,Review,Doctor

# Create your views here.
class DoctorViewSerializer(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class SpecializationViewSerializer(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewSerializer(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class DoctorAvailableTime(filters.BaseFilterBackend):
     def filter_queryset(self, request, queryset, view):
         doctor_id = request.query_params.get('doctor_id')
         if doctor_id is not None:
             queryset = queryset.filter(doctor=doctor_id)
         return queryset

class AvailableTimeViewSerializer(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [DoctorAvailableTime]

class ReviewViewSerializer(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer