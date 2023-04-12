from django.shortcuts import render
from django.views.generic import TemplateView


class template_test_view(TemplateView):
    template_name = 'base.html'
