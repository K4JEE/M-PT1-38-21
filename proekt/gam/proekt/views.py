from django.shortcuts import render, redirect
from proekt.models import Product as ProductModel
from proekt.models import Order
from proekt.forms import OrderForm
from django.views.generic import View
from proekt.utils import *

class Home(ObjectHomeMixin, View):
    template = 'home.html'

class Product(View):
    def get(self, request):
        products=ProductModel.objects.get()
        return render(request, 'product.html', {'products': products})

class Detail(ObjectDetailMixin,View):
    model = ProductModel
    template = "detail.html"

 
class Add(View):
    def get(self, request):

        form = OrderForm(request.POST, request.FILES)
        if request.method == "POST":

            if form.is_valid():

                order = Order()
            
                order.name = form.cleaned_data['name']
                order.surname = form.cleaned_data['surname']
                order.email = form.cleaned_data['email']
                order.address = form.cleaned_data['address']


                order.save()

                return redirect('order_done')
            else:
                form = OrderForm()

        return render(request, 'add.html')