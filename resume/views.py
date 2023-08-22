from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InformationsGenerales

# Create your views here.
class IndexView(TemplateView):
    template_name = 'resume.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        infogenerales = InformationsGenerales.objects.first()
        
        context["infogenerales"] = infogenerales
        return context
