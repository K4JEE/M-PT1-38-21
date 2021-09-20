from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm



def home (request):
    return render(request, 'home.html')

def product(request):
    products=Product.objects.all()
    return render(request, 'product.html', {'title': 'Станица с продукцией', 'products': products})

def detail(request, product_id):
    detail = Product.objects.get(id = product_id)
    return render(request, "detail.html",{'detail': detail})

def add(request):

    if request.method == "POST":

        form = OrderForm(request.POST, request.FILES)

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

    return render(request, 'add.html', {'add':add})