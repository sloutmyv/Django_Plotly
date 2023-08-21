from django.shortcuts import render
from django.views.generic import ListView
from .models import InformationsGenerales

# Create your views here.
class ProfilListView(ListView):
    template_name = 'resume.html'
    queryset = InformationsGenerales.objects.first()
    print(queryset)
