# Generated by Django 3.0.4 on 2020-12-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trpo', '0015_auto_20201218_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(choices=[('Ready set', 'Ready set'), ('Set', 'Set'), ('Wood', 'Wood'), ('Construction', 'Construction')], max_length=20),
        ),
    ]
