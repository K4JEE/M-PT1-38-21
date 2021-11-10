from django.shortcuts import render
from django.shortcuts import get_object_or_404
from proekt.models import Order
from proekt.forms import OrderForm


class ObjectHomeMixin:
    template = None
    def get(self,request):
        return render(request, self.template)


class ObjectProductMixin:
    model = None
    template = None

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, product_id):
        obj=get_object_or_404(self.model, id = product_id)
        return render(request, self.template, {self.model.__name__.lower(): obj})

    