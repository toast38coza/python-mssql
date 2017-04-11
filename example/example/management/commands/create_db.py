'''
Import from ics
'''
from django.core.management.base import BaseCommand
import os, pyodbc, time

class Command(BaseCommand):
    help = 'Create the initial DB'

    def handle(self, *args, **options):
        time.sleep(30) # wait for mssql container to be up / hack hackity hack hack
        db_name = os.environ.get('DB_NAME')
        sql = 'create database "{}"' . format (db_name)
        pwd = os.environ.get('SA_PASSWORD')
        connection_string = "driver=FreeTDS;server=db;PORT=1433 database=master;UID=sa;PWD={};TDS_Version=8.0;".format(pwd)

        conn = pyodbc.connect(connection_string, autocommit=True)
        conn.execute(sql)

        print('Created db: {}' . format(db_name))
