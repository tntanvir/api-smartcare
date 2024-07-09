from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contect


class ContectViewSet(viewsets.ModelViewSet):
    queryset = Contect.objects.all()
    serializer_class = ContactSerializer
