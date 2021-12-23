from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sphere, Cylinder, Cone, RectangularPrism, TriangularPrism
from .forms import CylinderForm, SphereForm, ConeForm, RectangularForm, TriangularForm

class HomePageView(TemplateView):
    template_name = "homepage.html"
    
#class SphereView(TemplateView):
 #   model = Sphere
  #  template_name= "sphere.html"

def CalcSphere(request):
    model = Sphere
    form = SphereForm()
    return render(request, 'sphere.html', {'form': form})

def Cylinder(request):
    model = Cylinder
    form = CylinderForm()
    return render(request, 'cylinder.html', {'form': form})

def Cone(request):
    model = Cone
    form = ConeForm()
    return render(request, 'cone.html', {'form': form})

def Rectangular(request):
    model = Rectangular
    form = RectangularForm()
    return render(request, 'rectangular.html', {'form': form})

def Triangular(request):
    model = Triangular
    form = TriangularForm()
    return render(request, 'triangular.html', {'form': form})
