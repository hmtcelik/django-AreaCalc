from django.db import models

class Sphere(models.Model):
    radius = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    pi = models.DecimalField(default=3.14, max_digits=20, decimal_places=10)

    @property
    def area(self):
        return self.radius * self.radius * self.pi

class Cylinder(models.Model):
    radius = models.FloatField(default=0, max_length=30)
    pi = models.FloatField(default=3.14, max_length=20)
    h = models.FloatField(default=0, max_length=30)
    
class Cone(models.Model):
    radius = models.FloatField(default=0, max_length=30)
    pi = models.FloatField(default=3.14, max_length=20)
    h = models.FloatField(default=0, max_length=30)
    s = models.FloatField(default=0, max_length=30)

class RectangularPrism(models.Model):
    h = models.FloatField(default=0, max_length=30)
    w = models.FloatField(default=0, max_length=30)
    l = models.FloatField(default=0, max_length=30)
    
class TriangularPrism(models.Model):
    b = models.FloatField(default=0, max_length=30)
    h = models.FloatField(default=0, max_length=30)
    l = models.FloatField(default=0, max_length=30)
    s = models.FloatField(default=0, max_length=30)