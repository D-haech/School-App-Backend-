from django.contrib import admin
from .models import School, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(School)