from django.contrib import admin
from main.models import Employee


@admin.register(Employee)   
class OranizationAdmin(admin.ModelAdmin):
    """by what parameters will the filter be in django admin"""
    list_display = ('full_name','parent','position','salary',)
    list_filter = [('position'),('level')]
