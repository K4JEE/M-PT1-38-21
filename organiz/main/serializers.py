from rest_framework import serializers
from main.models import Employee


class ListEmployeeSerializer(serializers.ModelSerializer):
    """which fields to display from the database"""
    class Meta:
        model = Employee
        fields = ('full_name','position','date_of_employment','parent','level')




