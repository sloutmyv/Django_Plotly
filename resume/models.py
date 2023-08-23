from ckeditor.fields import RichTextField
from datetime import date
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

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

class Experiences(models.Model):
    fonction = models.CharField('Fonction', max_length=200)
    entreprise = models.CharField('Entreprise', max_length=200)
    localisation = models.CharField('Localisation', max_length=200)
    description = RichTextField(blank=True, null=True)
    date_debut = models.DateField('Date de début')
    date_fin = models.DateField('Date fin',blank=True, null=True)
    secteurs = TaggableManager()
    is_today = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Expérience'
        verbose_name_plural = 'Expériences'
        ordering = ["-date_debut"]

    def __str__(self):
        return self.fonction

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.fonction)
        super(Experiences, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/experiences/{self.slug}"

class Formations(models.Model):
    ecole = models.CharField('Ecole', max_length=200)
    localisation = models.CharField('Localisation', max_length=200)
    description = RichTextField(blank=True, null=True)
    date_debut = models.DateField('Date de début')
    date_fin = models.DateField('Date fin',blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'
        ordering = ["-date_debut"]

    def __str__(self):
        return self.ecole

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.ecole)
        super(Formations, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/ecoles/{self.slug}"

class Skills(models.Model):
    skill = models.CharField('Compétence', max_length=200)

    class Meta:
        verbose_name = 'Compétence'
        verbose_name_plural = 'Compétences'
        ordering = ["skill"]

    def __str__(self):
        return self.skill
