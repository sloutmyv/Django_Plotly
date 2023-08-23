from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.
class InformationsGenerales(models.Model):
    first_name = models.CharField('Prénom', max_length=200)
    last_name = models.CharField('Nom', max_length=200)
    birth_date = models.DateField('Date de naissance')
    email = models.EmailField('Email')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Téléphone', validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    img = models.ImageField('Photo de profil', null=True, blank=True, upload_to="resume/images/" )
    linkedin_resume = models.URLField('LinkedIn URL',null=True, blank = True, max_length=200)
    adress = models.CharField('Adresse', null=True, blank = True, max_length=200)

    class Meta:
        verbose_name = 'Informations générales'
        verbose_name_plural = 'Informations générales'
    
    def __str__(self):
        return self.first_name + " " + self.last_name