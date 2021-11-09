from django.urls import path
from proekt.views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/', Product.as_view(), name='product'),
    path('add/', Add.as_view(), name='add'),
    path('<int:product_id>/', Detail.as_view() , name='detail'),
]