from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('eco/', include('eco.urls')),
    path('trpo/', include('trpo.urls')),
    # path('bestroy/', include('belstroy.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
