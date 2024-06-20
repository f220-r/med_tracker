from django.contrib import admin
from .models import User
from .models import Equipment
from .models import Report

# Register your models here.
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Report)