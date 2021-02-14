from django.contrib import admin
from .models import Exhibition, Exhibit, Master


admin.site.register(Exhibit)
admin.site.register(Exhibition)
admin.site.register(Master)