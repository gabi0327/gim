from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    seleccion_produccion = models.BooleanField(default=False)
    seleccion_recursos_humanos = models.BooleanField(default=False)

    
class Nombre(User):
    # Aquí puedes agregar campos adicionales si es necesario
    pass


