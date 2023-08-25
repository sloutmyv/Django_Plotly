from django.views.generic import TemplateView
from .models import InformationsGenerales, Experiences, Formations, Skills, Hobbies

# Create your views here.
class IndexView(TemplateView):
    template_name = 'resume/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        infogenerales = InformationsGenerales.objects.first()
        experiences = Experiences.objects.order_by('-date_debut')
        formations = Formations.objects.order_by('-date_debut')
        skills = Skills.objects.order_by('skill')
        hobbies = Hobbies.objects.order_by('hobbie')

        context["infogenerales"] = infogenerales
        context["experiences"] = experiences
        context["formations"] = formations
        context["skills"] = skills
        context["hobbies"] = hobbies

        return context
