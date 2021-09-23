from django.db import models
from datetime import datetime

# Create your models here.


class Rooms(models.Model):
    CATEGORY = (
    ("Superior","Superior"),
    ("Superior Ejecutiva","Superior Ejecutiva"),
    ("Royal 2 Cama","Royal 2 Cama"),
    ("Royal 1 Cama","Royal 1 Cama"),
    ("HoneyMoon Suite","HoneyMoon Suite"),
    ("Caribe Suite","Caribe Suite"),
    )

    DISTINCIONES = (
    ("1 Cama","1 Cama"),
    ("2 Cama","2 Cama"),
    ("2 Cama + silla","1 Cama + silita"),
    ("2 Cama + escritorio","1 Cama + escritorio"),
    ("Balcon","Balcon"),
    ("Suite con Jacuzzi","Suite con Jacuzzi"),
    ("Suite","Suite"),
    )

    ESTADO = (
        ("Ocupado","Ocupado"),
        ("Sucia","Sucia"),
        ("Mantimiento","Mantenimiento"),
        ("Bloqueada","Bloqueada"),
        ("Libre","Libre"),
    )

    numero = models.CharField(max_length=50)
    category = models.CharField( max_length=200,null=True,choices=CATEGORY)
    distinciones = models.CharField( max_length=200,null=True,choices=DISTINCIONES)
    estado = models.CharField( max_length=200,null=True,choices=ESTADO)
    piso = models.ForeignKey("Floor", on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Floor (models.Model):
    PISO = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    )
    piso = models.CharField(max_length=200,null=True,choices=PISO)

    def __str__(self):
        return self.piso

class Gym (models.Model):
    habitacion = models.CharField(max_length=50,null=True)
    nombre = models.CharField(max_length=200,null=True)
    date = models.DateField(null=True)
    timestart = models.TimeField(null=True)
    timeend = models.TimeField(null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Gym'
        verbose_name_plural = 'Gyms'