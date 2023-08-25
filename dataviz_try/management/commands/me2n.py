import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from dataviz_try.models import ME2NModel
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = 'shape and load from me2n csv file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'ME2N.xlsx'

        df = pd.read_excel(datafile, sheet_name='ME2N')
        df['COMMANDE']=df['COMMANDE'].astype(str)
        df['ARTICLE']=df['ARTICLE'].astype(str).str[:-2]
        df = df.reset_index()
        
        df = df.rename(columns={'index': 'id','DATE':'date_commande','COMMANDE':'num_commande',\
                                'ARTICLE':'code_article','DESIGNATION':'designation','QTE':'quantite',\
                                    'DEVISE':'devise','PRIX_U':'prix','VALEUR':'valeur','FOURNISSEUR':'fournisseur',})
        df.id += 1 
        
        print(df)
        
        engine = create_engine('sqlite:///db.sqlite3')

        df.to_sql(ME2NModel._meta.db_table, if_exists='replace',con=engine, index=False)
