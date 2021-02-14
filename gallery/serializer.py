from rest_framework import serializers
from .models import Exhibition, Exhibit, Master


class MasterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Master
        fields = ('name', 'second_name')


class ExhibitSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Exhibit
        fields = ('exhibits_name', 'masters_name', 'exhibits_type', 'style', 'creations_year', 'cost')


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('exhibits', 'description', 'exhibitions_date', 'start_time', 'end_time')