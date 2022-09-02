from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# function-based views
# def hello_world(request):
#     return HttpResponse("Hello World!")

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
