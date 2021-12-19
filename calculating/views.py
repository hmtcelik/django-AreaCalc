from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sphere, Cylinder, Cone, RectangularPrism, TriangularPrism
from .forms import SphereForm

class HomePageView(TemplateView):
    template_name = "homepage.html"
    
#class SphereView(TemplateView):
 #   model = Sphere
  #  template_name= "sphere.html"

def CalcSphere(request):
    form = SphereForm()
    return render(request, 'sphere.html', {'form': form})