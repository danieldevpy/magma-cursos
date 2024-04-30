from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/', include('model.urls')),
    path('certificate/', include('certificate.urls')),
    path('dash/', include('dash.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
