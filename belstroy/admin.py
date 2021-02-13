from django.contrib import admin
from .models import Goods
from .models import Help
from .models import Order
from .models import Index


admin.site.register(Goods)
admin.site.register(Help)
admin.site.register(Order)
admin.site.register(Index)
