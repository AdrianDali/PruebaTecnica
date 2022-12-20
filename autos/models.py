from django.db import models

class Marca(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Create your models here.
class Auto(models.Model):
    
    marca_auto = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


