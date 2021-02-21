from django.shortcuts import render
from rest_framework import viewsets
from .models import Exhibition
from .models import Exhibit, Master
from .serializer import ExhibitionSerializer, ExhibitSerializer, MasterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request


class ExhibitionsViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]