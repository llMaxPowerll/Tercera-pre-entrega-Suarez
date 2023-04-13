from django.db import models

# Create your models here.

class libro(models.Model):
    titulo=models.CharField(max_length=50)
    editorial=models.CharField(max_length=50)
    paginas=models.IntegerField()

    def __str__(self):
        return self.titulo+ "de" + self.editorial 
   
    class meta:
        verbose_name_plural='Libros'    
    
class biblioteca(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
 
    def __str__(self):
        return self.nombre
    

class autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombre + self.apellido
    
    class meta:
        verbose_name_plural='Autores'