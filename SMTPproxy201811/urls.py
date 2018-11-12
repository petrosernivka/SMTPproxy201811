from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('mainApp.urls')),
    path('send_mail/', include('send_mail.urls')),
    path('view_mail/', include('view_mail.urls')),
]
