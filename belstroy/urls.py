from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('goods/', views.Goods.as_view(), name='goods'),
    path('order/', views.Order.as_view(), name='order'),
    path('help/', views.Help.as_view(), name='help'),
]