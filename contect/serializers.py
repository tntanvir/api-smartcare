from rest_framework import serializers
from .models import Contect

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contect
        fields='__all__'
