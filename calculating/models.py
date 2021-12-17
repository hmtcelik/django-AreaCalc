from django.db import models

class Sphere(models.Model):
    radius = models.FloatField(default=0)
    pi = models.FloatField(default=3.14)

class Cylinder(models.Model):
    radius = models.FloatField(default=0)
    pi = models.FloatField(default=3.14)
    h = models.FloatField(default=0)
    
class Cone(models.Model):
    radius = models.FloatField(default=0)
    pi = models.FloatField(default=3.14)
    h = models.FloatField(default=0)
    s = models.FloatField(default=0)

class RectangularPrism(models.Model):
    h = models.FloatField(default=0)
    w = models.FloatField(default=0)
    l = models.FloatField(default=0)
    
class TriangularPrism(models.Model):
    b = models.FloatField(default=0)
    h = models.FloatField(default=0)
    l = models.FloatField(default=0)
    s = models.FloatField(default=0)