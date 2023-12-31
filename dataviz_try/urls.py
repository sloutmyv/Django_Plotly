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
from django.conf import settings
from django.conf.urls.static import static
from .views import DatavizView
from django.views.generic import TemplateView

app_name = "dataviz_try"

urlpatterns = [
    path("", DatavizView.as_view(), name='dataviztry-view'),
    path("contexte/", TemplateView.as_view(template_name="dataviz_try/contexte.html"), name='contexte'),
    path("food_trade/", TemplateView.as_view(template_name="dataviz_try/food_trade.html"), name='food-trade'),
    path("food_security/", TemplateView.as_view(template_name="dataviz_try/food_security.html"), name='food-security'),
    path("fruits_legumes_nc/", TemplateView.as_view(template_name="dataviz_try/fruits_legumes_nc.html"), name='fruits-legumes-nc'),
    path("prix_alimentation_nc/", TemplateView.as_view(template_name="dataviz_try/prix_alimentation_nc.html"), name='prix-alimentation-nc'),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
