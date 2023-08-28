from django.shortcuts import render
from django.views.generic import FormView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm

# Create your views here.
class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/message-envoye/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        subject = "Django Dataviz - Contact form request" 
        cc_myself = form.cleaned_data['cc_myself']
        body = {
			'name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email'], 
			'content': form.cleaned_data['content'], 
			}
        message = "\n".join(body.values())
        list_destinataire = ['clerc.sylv@gmail.com']
        if cc_myself:
            list_destinataire.append(body['email'])
        try:
            send_mail(subject, message, body['email'], list_destinataire) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return super(ContactView, self).form_valid(form)