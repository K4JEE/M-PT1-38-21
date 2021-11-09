from django.shortcuts import render, redirect
from proekt.models import Product as ProductModel
from proekt.models import Order
from proekt.forms import OrderForm
from django.views.generic import View
from django.shortcuts import get_object_or_404


class Home(View):
    def get(self,request):
        return render(request, 'home.html')


class Product(View):
    def get(self, request):
        products=ProductModel.objects.all()
        return render(request, 'product.html', {'title': 'Станица с продукцией', 'products': products})

class Detail(View):
    def get(self, request, product_id):
        detail = get_object_or_404(ProductModel, id = product_id )
        return render(request, "detail.html",{'detail': detail})


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