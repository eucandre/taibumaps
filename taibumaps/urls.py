from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('app_user.urls')),
    path('farms/', include('app_fazenda.urls'), name='farms'),
    path('maps/', include('app_mapa.urls'), name='maps'),
    path('files/', include('app_files.urls'), name='files'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('app_user.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
