from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InformationsGenerales, Experiences

# Create your views here.
class IndexView(TemplateView):
    template_name = 'resume.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        infogenerales = InformationsGenerales.objects.first()
        experiences = Experiences.objects.order_by('-date_debut')
        
        context["infogenerales"] = infogenerales
        context["experiences"] = experiences
        
        return context
