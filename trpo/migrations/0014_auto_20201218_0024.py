# Generated by Django 3.0.4 on 2020-12-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trpo', '0013_auto_20201218_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(choices=[('A', 'Author'), ('E', 'Editor')], max_length=20),
        ),
    ]
