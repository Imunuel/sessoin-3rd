from django.db import models
from django.urls import reverse


class Goods(models.Model):
    photo = models.ImageField(upload_to='trpo')#, verbose_name='Фото')
    about_product = models.CharField(max_length=280)#, verbose_name='О продукте')
    price = models.IntegerField(default=0)#, verbose_name='Цена')
    # code = models.IntegerField(default=0, verbose_name='Код товара')
    category = models.CharField(max_length=20, choices=[('Ready set', 'Ready set'), ('Set', 'Set'), ('Wood', 'Wood'), ('Construction', 'Construction')])#, verbose_name='Категория')

    def __str__(self):
        return ('Code item: ' + str(self.id) + ' | Category: ' + self.category)

    class Meta:
        ordering = ('category', 'id')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    name = models.CharField(max_length=100)#, verbose_name='Имя')
    location = models.CharField(max_length=100)#, verbose_name='Адрес')
    telephon = models.CharField(max_length=13)#, verbose_name='Телефон')
    goods = models.ManyToManyField(Goods)#, verbose_name='Товары')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_absolute_url(self):
        return reverse('goods')


class Help(models.Model):
    name = models.CharField(max_length=100, blank=True)#, verbose_name='Имя')
    email = models.EmailField(max_length=30)#, verbose_name='Почта')
    telephon = models.CharField(max_length=13)#, verbose_name='Телефон')
    message = models.TextField()#verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'

    def get_absolute_url(self):
        return reverse('index')


class Index(models.Model):
    article = models.CharField(max_length=100, verbose_name='Заголовок')
    about = models.TextField(verbose_name='О нас')

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'