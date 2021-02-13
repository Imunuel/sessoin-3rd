from django.db import models
from django.urls import reverse


class Goods(models.Model):
    photo = models.ImageField(upload_to='trpo')
    about_product = models.CharField(max_length=280)
    price = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    category = models.CharField(max_length=20)

    def __str__(self):
        return ('Код товара:' + str(self.code))


class Order(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    telephon = models.CharField(max_length=10)
    goods = models.ManyToManyField(Goods)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Help(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=30)
    telephon = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Index(models.Model):
    article = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.article