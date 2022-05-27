from django.shortcuts import render
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer

class PersonaViewset(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer