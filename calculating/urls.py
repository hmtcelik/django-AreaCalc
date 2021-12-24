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
from .views import HomePageView, SphereCalc, CylinderCalc, ConeCalc, RectangularCalc, TriangularCalc, ContactView, PyramidCalc

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path("sphere/", views.SphereCalc.as_view(), name="sphere"),
    path("cylinder/", views.CylinderCalc.as_view(), name="cylinder"),
    path("cone/", views.ConeCalc.as_view(), name="cone"),
    path("rectangular/", views.RectangularCalc.as_view(), name="rectangular"),   
    path("triangular/", views.TriangularCalc.as_view(), name="triangular"),
    path("pyramid/", views.PyramidCalc.as_view(), name="pyramid"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    ]
