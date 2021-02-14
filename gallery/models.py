from django.db import models
import time

class Master(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)

    def __str__(self):
        return (self.name + ' ' + self.second_name)


class Exhibit(models.Model):
    exhibits_name = models.CharField(max_length=50)
    masters_name = models.ForeignKey(Master, on_delete=models.CASCADE)
    exhibits_type = models.CharField(max_length=15, choices=[('painting', 'Painting'),('sculpture','Sculpture')])
    style = models.CharField(max_length=15, choices=[('realism','Realism')])
    creations_year = models.DateField()
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.exhibits_name


class Exhibition(models.Model):
    exhibits = models.ManyToManyField(Exhibit)
    description = models.TextField()
    exhibitions_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.exhibitions_date)