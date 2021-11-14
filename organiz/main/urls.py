from django.urls import path
from main.views import *


urlpatterns = [
    path('all/', AllEmployeeListView.as_view()),
    path('gendir/', GenDirectorListView.as_view()),
    path('dir/', DirectorListView.as_view()),
    path('top/', TopManagerListView.as_view()),
    path('manager/', ManagerListView.as_view()),
    path('employee/', EmployeeListView.as_view()),

]
