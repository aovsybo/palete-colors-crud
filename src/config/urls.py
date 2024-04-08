from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.api.urls')),
    path('paletes/', include('paletes.api.urls')),
] + yasg_urls
