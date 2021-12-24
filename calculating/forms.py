from django import forms


class SphereForm(forms.Form):
        
    r = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    pi = forms.DecimalField(max_digits=20, decimal_places=10, initial=3.14, required=False)
   
class CylinderForm(forms.Form):
        
    r = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    h = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    pi = forms.DecimalField(max_digits=20, decimal_places=10, initial=3.14, required=False)

    
class ConeForm(forms.Form):
        
    r = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    s = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    h = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    pi = forms.DecimalField(max_digits=20, decimal_places=10, initial=3.14, required=False)
   
class RectangularForm(forms.Form):
        
    l = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    w = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    h = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
   
class TriangularForm(forms.Form):
        
    l = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    s = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    b = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    h = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    
class PyramidForm(forms.Form):
        
    b = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    s = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
    h = forms.DecimalField(max_digits=20, decimal_places=10, initial=0, required=False)
   
        
