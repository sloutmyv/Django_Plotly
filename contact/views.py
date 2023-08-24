from django.shortcuts import render
from django.views.generic import FormView
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/message-envoye/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        # subject = form.cleaned_data["name"]
        # sender = form.cleaned_data["email"]
        # message = form.cleaned_data["content"]
        # cc_myself = form.cleaned_data["cc_myself"]
        #
        # recipients = ["clerc.sylv@gmail.com"]
        # if cc_myself:
        #     recipients.append(sender)
        #
        # send_mail(subject, message, sender, recipients)

        return super(ContactView, self).form_valid(form)
