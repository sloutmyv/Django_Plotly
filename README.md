# Django app for Pacific Dataviz 2023 Challenge

## Langage de programation
Installer le langage [Python](https://www.python.org/downloads/)
## Editeur de texte
Installer l'éditeur [Visual studio](https://code.visualstudio.com/) 

Install pip package for vs studio extensions : 
```
pip install autopep8 
pip install pylint
pip install django-pylint
```

Install VS Code extensions : 
- Python/Pylance
- SQlite
- Django
- PowerShell
- Markdown Preview Enhancer

## Github
Pour chaque nouveau projet créer un répertoire directement depuis le [GitHub](https://github.com/)
### Les commandes à connaitre 
Pour cloner un répertoire existant depuis github : 
```
git clone <url>
```
Pour afficher la liste des fichiers/dossiers modifiés : 
```
git status
```
Pour ajouter des fichiers/dossiers non inclus : 
```
git add <fichier/dossier>
git add .
```
Pour créer un commit : 
```
git commit -m “description du commit”
```
Pour uploader les modifications sur github (sur la branche master) : 
```
git push origin master
```
Pour extraire mettre à jour le dossier depuis githup : 
```
git fetch origin
```
Pour fusionner depuis github : 
```
git pull
```
Pour lister les commits (taper q pour quitter) : 
```
git log 
```

### Le fichier ".gitignore"
Il est créé à la racine du projet pour indiquer les fichier à ne pas upload sur le répertoire github en ligne, à inclure (pour un projet Django):
```
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
db.sqlite3-journal
media/
static/

# python-decouple
settings.ini

# Data
data/
```

## Environnement virtuel
Installer le package d’environnement virtuel : 
```
pip install virtualenv
```
Creer l’environnement virtuel : 
```
python -m venv <virtual-environnement-name>
```
Activer l’environnement virtuel : 
- Linux/Mac :
```
source <virtual-environnement-name>/bin/activate
```
- Windows :
```
Set-ExecutionPolicy Unrestricted -Scope Process (si fontionne pas)
env\Scripts\activate
```
Désactiver l’environnement virtuel :
``` 
deactivate
```

## Installer les Packages : 
```
pip install <some-dependance>
```
Lister les dépendances : 
```
pip freeze
```
Ajouter les dépendances à un fichier “requirement.txt”
```
pip freeze > requirement.txt
```
Installer les dépendances présentes dans un fichier “requirement.txt” : 
```
pip install -r requirement.txt
```

## Django Project
Créer un projet : 
```
django-admin startproject <newproject>
```

>Make sure to protect secrets_keys with "python-decouple" module.
- En développement : avec un fichier settings.ini à inscrire dans le fichier .gitignore puis en production 
- En prod : You can go to your Heroku dashboard, click on your app, go to your apps settings, and see the "Config Vars" section and click "Reveal Vars" or "Add Vars" and add your SECRET_KEY there.

### Les applications 

Créer une application dans le projet : 
```
python manage.py startapp <newapp>
```

Une fois créée, il faut ajouter l’application dans newproject/settings.py/INSTALLED_APP (surtout si des modèles sont créés)

**Workflow basic :** 

1. Ajouter un fichier urls.py dans l’application
1. Référencer ce fichier dans le fichier d’urls global 
1. Créer la vue associée (celle qui sera appelée)
1. Créer le template html associé à cette vue

L’url appel une vue, la vue appel un template et éventuellement un model (pour extraire des données GET) ou un formulaire (pour poster des données POST).

### Les modèles 

Les modèles permettent de stocker des données dans une base de donnée.
L’imputation de la base de donnée peut se faire avec une fonction (BaseCommand) ou bien par un template accéssible à l’admin ou bien par un formulaire sur le site.

### Les formulaires 

Les formulaires sont associés à des modèles pour imputer des données dans une base de données directement depuis l'application (ou l'admin)

### Les vues 

Les vues sont créées dans chaque application dans le fichier views.py
Elles peuvent être écrites sous forme de fonction ou de class.
Généralement elles renvoient un template et un contexte qui est un ensemble d’attribut retournable dans le template.

Généralement le context est un queryset d’un model. Il est alors possible de “filtrer” le modèle selon le queryset passé.

https://docs.djangoproject.com/en/4.2/ref/class-based-views/

### Les templates 
fichiers html

### Le style 
fichiers css

### Les “statics” 
Static file : 
- css
- js
- img “imported” by the dev

Lors du développement les fichiers static et les médias peuvent être gérer d’abord en local puis transférer à un serveur web type aws s3 avant le déploiement.

###Les “medias” 
Media file :
- file/img “imported” through a model with ImageField or FileField stored in database.

###La base de donnée 

Ne pas oublier de mettre les applications dans settings/INSTALLED_APPS

Pour préparer les migrations : 
```
python manage.py makemigrations
```
Pour migrer : 
```
python manage.py migrate
```

Au cas ou cela ne fonctionne pas :
``` 
python manage.py migrate –run_syncdb
```

## Go Live

### AWS S3 as a web server :
for static and media files à faire avant le déploiement
Utilisation ASW : https://youtu.be/ahBG_iLbJPM?si=us7zk-C409govBZo

**Mode opératoire Sur le site AWS3 :**
- Dans la console selectionner le service S3
- Créer un compartiment : "Your-bucket"
- Désactiver “ bloquer tous les accès publique “ car il s”agit d’un hébergement de static pour un site internet.
- Service “IAM”
- Créer un nouveau groupe "your-group". Associé la politique d’utilisation : “AmazonS3FullAccess” car l’utilisateur à besoin d’upload/download des données : 
- Créer un utilisateur à l’associer au groupe
- Créer un clé d’accès : “Application exécutées en dehors d’AWS” et les copier dans settings.ini

Dans l’environnement virtuel :
``` 
pip install boto3
pip install django-storages
``` 

Dans settings.py et settings.ini : 
``` 
voir exemple
``` 

Lancer :
``` 
python manage.py collectatics
``` 

### Heroku for hosting
Local web app → github → Heroku platform
La mise à jour du repo github permet la mise à jour de l’application sur heroku
Déploiement sur heroku https://youtu.be/2OHc5EqfX5g?si=2weTY9HA3WDkLjYM

Le basculement sur la bdd postgrsql se fait directement sur heroku avant de cloner le repo.

Une fois la base postgr créée, on peut charger la base de donnée avec les fonctions de management directement. 

### Domain name



## Le Challenge Dataviz 

Deux catégorie : **Statique & Interactive** 

Le thème : **Nourriture**

Critères d’évaluations : 
- storytelling : raconter une histoire percutante et engageante pour le lecteur 
- Design
- Innovation 
- Solution technique et profondeur analytique

Les base de données : 
Pacific Data Hub : 
- [Pacific Food Trade](https://stats.pacificdata.org/vis?tm=trade&pg=0&snb=14&df[ds]=ds%3ASPC2&df[id]=DF_TRADE_FOOD&df[ag]=SPC&df[vs]=1.0&pd=%2C2018&dq=A.Q.AS%2BCK%2BFJ%2BFM%2BGU%2BKI%2BMH%2BMP%2BNC%2BNR%2BNU%2BPF%2BPG%2BPN%2BPW%2BSB%2BTK%2BTO%2BTV%2BVU%2BWF%2BWS.AU_NZ.10%2B11%2B12%2B15%2B16%2B17%2B18%2B19%2B20%2B21%2B22%2B24%2B02%2B03%2B04%2B07%2B08%2B09&ly[cl]=TIME_PERIOD&ly[rw]=COMMODITY&to[TIME_PERIOD]=false)
- [Food Security](https://stats.pacificdata.org/vis?tm=food%20security&pg=0&snb=17&df[ds]=ds%3ASPC2&df[id]=DF_FOOD_SECURITY_HIES_3&df[ag]=SPC&df[vs]=1.0&pd=%2C&dq=A........&ly[cl]=INDICATOR&ly[rw]=FOOD&to[TIME_PERIOD]=false)
Open Data NC : 
- [Marché des fruits et légumes en Nouvelle-Calédonie](https://data.gouv.nc/explore/?flg=fr&disjunctive.theme&disjunctive.publisher&disjunctive.keyword&disjunctive.attributions&disjunctive.license&sort=explore.popularity_score&refine.keyword=PacificDatavizChallenge2023&refine.attributions=%20Direction%20des%20Affaires%20V%C3%A9t%C3%A9rinaires,%20Alimentaires%20et%20Rurales%20(DAVAR))
- [Prix des produits alimentaires en Nouvelle-Calédonie](https://data.gouv.nc/explore/?flg=fr&disjunctive.theme&disjunctive.publisher&disjunctive.keyword&disjunctive.attributions&disjunctive.license&sort=explore.popularity_score&refine.attributions=Direction%20des%20Affaires%20%C3%89conomiques%20(DAE)&refine.keyword=PacificDatavizChallenge2023)