from django.db import models

# Create your models here.

class contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=True)
    apellidos = models.TextField(null=True)
    telefono= models.IntegerField(max_length=9)
    email = models.TextField(null=True)
    comentario = models.TextField(null=True)

    def __str__(self):
        fila = "Nombre: "+self.nombre+" "+self.apellidos
        return fila
    
    def delete(self, using=None, keep_parent=False):
        super().delete()