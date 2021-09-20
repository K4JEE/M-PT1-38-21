from django.db import models
from django.db.models.fields.files import ImageField


class Product(models.Model):
    
    title = models.CharField('название продукта', max_length=40)
    photo = models.ImageField(upload_to='uploads')
    content = models.TextField('описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Товар'
        verbose_name_plural= 'Товары'


class Order(models.Model):

    user = models.CharField(max_length=255)
    items = models.CharField(max_length=1000, blank=False)
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    city = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=True)


