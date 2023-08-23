from django.contrib import admin
from .models import InformationsGenerales, Experiences

# Register your models here.

@admin.register(InformationsGenerales)
class InformationsGeneralesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
        form_instance.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
        form_instance.fields['birth_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        form_instance.fields['email'].widget.attrs['placeholder'] = 'example@email.com'
        form_instance.fields['phone_number'].widget.attrs['placeholder'] = '+687XXXXXX'
        return super().render_change_form(request, context, *args, **kwargs)

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display=['fonction', 'entreprise','date_debut','date_fin']