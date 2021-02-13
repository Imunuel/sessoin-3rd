from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView 
from .models import Help
from .models import Order
from .models import Goods
from .models import Index


class Index(ListView):
    model = Index
    context_object_name = 'Index' 
    template_name = 'trpo/index.html'

   
class Goods(ListView):
    model = Goods
    context_object_name = 'Goods' 
    template_name = 'trpo/items.html'


class Order(CreateView):
    model = Order
    template_name = 'trpo/order.html'
    fields = ['name', 'location', 'telephon', 'goods']


class Help(CreateView):
    model = Help
    template_name = 'trpo/help.html'
    fields = ['name', 'email', 'telephon', 'message']