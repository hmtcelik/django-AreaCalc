"""Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import HomePageView, CalcSphere, Cylinder, Cone, Rectangular, Triangular

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    #path("sphere/", SphereView.as_view(), name="sphere"),
    path("sphere/", views.CalcSphere, name="sphere"),
    path("cylinder/", views.Cylinder, name="cylinder"),
    path("cone/", views.Cone, name="cone"),
    path("rectangular/", views.Rectangular, name="rectangular"),
    path("triangular/", views.Triangular, name="triangular"),
    ]
