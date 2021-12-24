from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SphereForm, CylinderForm, ConeForm, RectangularForm, TriangularForm, PyramidForm

class HomePageView(TemplateView):
    template_name = "homepage.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"
    
    
    



# 3D objects views    

####################################################################
class SphereCalc(TemplateView):
    template_name = 'sphere.html'

    def get(self, request, *args, **kwargs):
        form = SphereForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = SphereForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['r']
            b = form.cleaned_data['pi']
            volume = 4*b*a*a*a/3
            area = 4*b*a*a
            form = SphereForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )
    
####################################################################
class CylinderCalc(TemplateView):
    template_name = 'cylinder.html'

    def get(self, request, *args, **kwargs):
        form = CylinderForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = CylinderForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data['r']
            h = form.cleaned_data['h']
            p = form.cleaned_data['pi']
            
            volume = p*r*r*h
            area = (2*p*r*r) + (2*p*r*h)
            form = CylinderForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )

####################################################################    
class ConeCalc(TemplateView):
    template_name = 'cone.html'

    def get(self, request, *args, **kwargs):
        form = ConeForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = ConeForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data['r']
            h = form.cleaned_data['h']
            p = form.cleaned_data['pi']
            s = form.cleaned_data['s']

            volume = p*r*r*h/3
            area = (p*r*s) + (p*r*r)
            form = ConeForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )
 
####################################################################  
class RectangularCalc(TemplateView):
    template_name = 'rectangular.html'

    def get(self, request, *args, **kwargs):
        form = RectangularForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = RectangularForm(request.POST)
        if form.is_valid():
            l = form.cleaned_data['l']
            w = form.cleaned_data['w']
            h = form.cleaned_data['h']

            volume = 2*((l*w)+(l*h)+(w*h))
            area = l*w*h
            form = RectangularForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )
  
####################################################################    
class TriangularCalc(TemplateView):
    template_name = 'triangular.html'

    def get(self, request, *args, **kwargs):
        form = TriangularForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = TriangularForm(request.POST)
        if form.is_valid():
            l = form.cleaned_data['l']
            s = form.cleaned_data['s']
            b = form.cleaned_data['h']
            h = form.cleaned_data['h']

            volume = (b*h)+(2*l*s)+(l*b)
            area = b*h*l/2
            form = TriangularForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )
    
####################################################################    
class PyramidCalc(TemplateView):
    template_name = 'pyramid.html'

    def get(self, request, *args, **kwargs):
        form = PyramidForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = PyramidForm(request.POST)
        if form.is_valid():
            b = form.cleaned_data['b']
            s = form.cleaned_data['s']
            h = form.cleaned_data['h']

            volume = b*b*h/3
            area = (b*b)+2*b*s
            form = PyramidForm()
            #return redirect ('home:home')

        args = {'form': form , 'volume': volume, 'area': area}
        return render(request, self.template_name, args )
    
    



