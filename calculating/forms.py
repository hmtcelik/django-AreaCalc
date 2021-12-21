from django import forms
from .models import Sphere, Cylinder, Cone, RectangularPrism, TriangularPrism


class SphereForm(forms.ModelForm):
    
    class Meta:
        model = Sphere
        fields = ('radius','pi',)
        
        
