from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


my_choices =( 
    ('GenDir','GenDirector'),
    ('Dir','Director'),
    ('Top','TopManager'),
    ('Manager','Manager'),
    ('Employee','Employee')
)
class Employee(MPTTModel): 
    """creates a tree structure"""
    full_name = models.CharField(verbose_name='ФИО',max_length=50, unique=True)
    position = models.CharField(verbose_name='Должность', choices=my_choices, max_length=10, default=None)
    salary = models.IntegerField(verbose_name='Заработная плата')
    date_of_employment= models.DateField(verbose_name='Дата устройства на работу',default=False)
    parent = TreeForeignKey('self',verbose_name='Начальник', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return str(self.id) + ':' + self.full_name

    class MPTTMeta:
        order_insertion_by = ['full_name']
