from django.contrib import admin
from .models import InformationsGenerales

# Register your models here.

@admin.register(InformationsGenerales)
class InformationsGeneralesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)