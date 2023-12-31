"""
URL configuration for Django_Plotly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "main"

urlpatterns = [
    path("", TemplateView.as_view(template_name="main/main_home.html"), name='home-page'),
    path("mentions-legales/", TemplateView.as_view(template_name="main/main_mentions.html"), name='mentions-legales'),
    path("politique-confidentialite/", TemplateView.as_view(template_name="main/main_politique.html"), name='politique-confidentialite'),
]
