from django.db import models
import os, sys
currentdir = os.path.dirname(os.path.abspath(__file__))

class StarSystem(models.Model):
    name = models.CharField(max_length=200)

class Planet(models.Model):
    name = models.CharField(max_length=200)
    starsystem = models.ForeignKey(StarSystem, on_delete=models.CASCADE)