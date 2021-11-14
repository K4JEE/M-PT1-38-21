from rest_framework import generics
from main.models import Employee
from main.serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class AllEmployeeListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of all employees with access rights granted through the django admin panel"""
    permission_required = 'main.view_employee'
    queryset = Employee.objects.all()
    serializer_class = ListEmployeeSerializer

class GenDirectorListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of employees of the same level. Access rights are issued through the django admin panel"""
    permission_required = 'main.view_employee'
    queryset = Employee.objects.filter(level='0')
    serializer_class = ListEmployeeSerializer

class DirectorListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of employees of the same level. Access rights are issued through the django admin panel"""
    queryset = Employee.objects.filter(level='1')
    serializer_class = ListEmployeeSerializer
    permission_required = 'main.view_employee'

class TopManagerListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of employees of the same level. Access rights are issued through the django admin panel"""
    queryset = Employee.objects.filter(level='2')
    serializer_class = ListEmployeeSerializer
    permission_required = 'main.view_employee'
    
class ManagerListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of employees of the same level. Access rights are issued through the django admin panel"""
    queryset = Employee.objects.filter(level='4')
    serializer_class = ListEmployeeSerializer
    permission_required = 'main.view_employee'

class EmployeeListView(PermissionRequiredMixin,generics.ListAPIView):
    """representation of employees of the same level. Access rights are issued through the django admin panel"""
    queryset = Employee.objects.filter(level='5')
    serializer_class = ListEmployeeSerializer
    permission_required = 'main.view_employee'
    

