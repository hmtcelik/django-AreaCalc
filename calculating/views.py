from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sphere, Cylinder, Cone, RectangularPrism, TriangularPrism

class HomePageView(TemplateView):
    template_name = "homepage.html"
    
class SphereView(TemplateView):
    template_name=
