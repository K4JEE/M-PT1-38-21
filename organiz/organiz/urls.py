from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/main/', include('main.urls')),


]
