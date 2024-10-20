from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class PageView(TemplateView):
    template_name = 'product-grid-sidebar-left.html'


class ErrorView(TemplateView):
    template_name = '404.html'


class AboutUs(TemplateView):
    template_name = 'about-us.html'

class ContactUs(TemplateView):
    template_name = 'contact.html'

class AccountPage(TemplateView):
    template_name = 'user-acount.html'

class LoginPage(TemplateView):
    template_name = 'user-login.html'

class RegisterPage(TemplateView):
    template_name = 'user-register.html'

class WishlistPage(TemplateView):
    template_name = 'user-wishlist.html'
