from django.db import models

field = [
        ('uci', 'UCI'),
        ('cardio','Cardiologia'),
        ('nefro','Nefrologia'),
        ('quiro','Quirofano'),
        ('radio','Radiologia'),
        ('gral','General')
    ]

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=8,blank=True)
    phone =  models.CharField(max_length=20, blank=True)
    role = [
        ('staff','Personal'),
        ('admin','Gerencia'),
        ('tech', 'Ingenieria'),
        ('med', 'Medicina'),
    ]
    sector = models.CharField(max_length=20, choices=role, default='staff')
    area = models.CharField(max_length=20, choices=field, default='gral')
    bio = models.TextField(blank=True)
    
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return (self.first_name+self.last_name)
    def save(self, *args, **kwargs):
        # Custom save method if needed
        super().save(*args, **kwargs)


class Equipment(models.Model):
    status = [
        ('op', 'En operacion'),
        ('cm', 'Mantenimiento correctivo'),
        ('pm','Mantenimiento preventivo'),
        ('os', 'Fuera de servicio')
    ]
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=150)
    fabrication_year = models.CharField(max_length=10)
    adquisition_year = models.CharField(max_length=10) 
    area = models.CharField(max_length=20, choices=field, default='gral')
    location = models.CharField(max_length=20, choices=field, default='gral')
    status = models.CharField(max_length=20,choices= status, default='op')


class Report(models.Model):
    status = [
        ('ir', 'En reparacion'),
        ('m', 'En Mantenimiento'),
        ('f','Reparado'),
        ('fm', 'Mantenimiento finalizado'),
        ('d', 'Enviado a deposito')
    ]
    report_id = models.CharField(max_length=50)
    equipment = models.ManyToManyField(Equipment)
    date_admitted = models.DateField(auto_now=True)
    technician = models.ManyToManyField(User)
    status = models.CharField(max_length=20,choices= status, default='op')
    commentary = models.CharField(max_length=500)
