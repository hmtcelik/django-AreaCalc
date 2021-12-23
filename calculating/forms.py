from django import forms
from .models import Sphere, Cylinder, Cone, RectangularPrism, TriangularPrism


class SphereForm(forms.ModelForm):
    
    class Meta:
        model = Sphere
        fields = ('radius','pi',)
        
class CylinderForm(forms.ModelForm):
    
    class Meta:
        model = Cylinder
        fields = ('radius','pi','h',)

class ConeForm(forms.ModelForm):
    
    class Meta:
        model = Cone
        fields = ('radius','pi','h','s',)
        
class RectangularForm(forms.ModelForm):
    
    class Meta:
        model = RectangularPrism
        fields = ('h','w','l',)
        
class TriangularForm(forms.ModelForm):
    
    class Meta:
        model = TriangularPrism
        fields = ('b','h','l','s',)
        
        
