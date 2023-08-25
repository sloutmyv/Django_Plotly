from django.db import models

# Create your models here.
class ME2NModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_commande = models.DateField('Date de commande')
    num_commande = models.CharField('Numéro commande', max_length=200)
    code_article = models.CharField('Code article', max_length=200)
    designation = models.CharField('Designation', max_length=200)
    quantite = models.FloatField('Quantité')
    devise = models.CharField('Devise', max_length=200)
    prix = models.FloatField('Prix')
    valeur = models.FloatField('Valeur')
    fournisseur = models.CharField('Fournisseur', max_length=200)


