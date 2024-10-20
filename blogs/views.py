from msilib.schema import ListView

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class BlogsView(TemplateView):
    template_name = 'blog-list-sidebar-right.html'
