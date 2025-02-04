from django.contrib import admin
from django.urls import path, include  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')), 
    path('main/', include('main.urls')), 
    path('message/', include('message.urls')), 
    path('mypage/', include('mypage.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)