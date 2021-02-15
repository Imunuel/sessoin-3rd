from django.shortcuts import render
from rest_framework import viewsets
from .models import Exhibition
from .models import Exhibit, Master
from .serializer import ExhibitionSerializer, ExhibitSerializer, MasterSerializer


class ExhibitionsViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


