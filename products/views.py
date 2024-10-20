from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class CheckoutPage(TemplateView):
    template_name = 'product-checkout.html'

class CartView(TemplateView):
    template_name = 'product-cart.html'
