from django.contrib import admin
from django.urls import path, include
from proekt import views as testAppViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testAppViews.home, name='home'),
    path('product/', testAppViews.product, name='product'),
    path('add/', testAppViews.add, name='add'),
    path('<int:product_id>/', testAppViews.detail , name='detail'),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)