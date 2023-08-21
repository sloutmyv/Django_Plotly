from django.contrib import admin
from .models import InformationsGenerales

# Register your models here.

class InformationsGeneralesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(InformationsGenerales, InformationsGeneralesAdmin)
