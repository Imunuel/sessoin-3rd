from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView 
from .models import Help
from .models import Order
from .models import Goods
from .models import Index


class Index(ListView):
    model = Index
    context_object_name = 'Index' 
    template_name = 'belstroy/index.html'


class Goods(ListView):
    model = Goods
    context_object_name = 'Goods' 
    template_name = 'belstroy/items.html'


class Order(CreateView):
    model = Order
    template_name = 'belstroy/order.html'
    fields = ['name', 'location', 'telephon', 'goods']


class Help(CreateView):
    model = Help
    template_name = 'belstroy/help.html'
    fields = ['name', 'email', 'telephon', 'message']