from django.db import models

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        txt = f"{descripcion}"
        return txt

    class Meta:
        verbose_name_plural = "Categorias"
    