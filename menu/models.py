from django.db import models

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    informacion_nutricional = models.TextField()
    fecha = models.DateField()
    calificacion_promedio = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.platillo.nombre}"
