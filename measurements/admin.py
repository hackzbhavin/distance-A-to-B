from django.contrib import admin
from .models import Measurement # from models.py class is fetched here
# Register your models here.

admin.site.register(Measurement)