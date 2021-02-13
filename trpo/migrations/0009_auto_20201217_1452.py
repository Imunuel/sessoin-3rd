# Generated by Django 3.0.4 on 2020-12-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trpo', '0008_auto_20201217_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='about_product',
            field=models.CharField(max_length=280, verbose_name='О продукте'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='code',
            field=models.IntegerField(default=0, verbose_name='Код товара'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
