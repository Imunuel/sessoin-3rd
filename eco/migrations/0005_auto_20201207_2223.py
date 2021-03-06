# Generated by Django 3.0.4 on 2020-12-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0004_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='CH_count',
        ),
        migrations.RemoveField(
            model_name='people',
            name='FSZN',
        ),
        migrations.RemoveField(
            model_name='people',
            name='TS',
        ),
        migrations.RemoveField(
            model_name='people',
            name='UF',
        ),
        migrations.RemoveField(
            model_name='people',
            name='accrued',
        ),
        migrations.RemoveField(
            model_name='people',
            name='tax',
        ),
        migrations.AlterField(
            model_name='people',
            name='count_old',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='people',
            name='count_young',
            field=models.IntegerField(default=0),
        ),
    ]
