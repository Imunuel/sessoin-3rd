from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView 
from .models import People


class ECO(ListView):
    model = People
    context_object_name = 'People' 
    template_name = 'eco/index.html'