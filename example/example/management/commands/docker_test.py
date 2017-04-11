'''
Import from ics
'''
from django.core.management.base import BaseCommand
from django.core.management import call_command
import os, pyodbc, time

class Command(BaseCommand):
    help = 'Create the initial DB'

    def handle(self, *args, **options):
        time.sleep(30) # wait for mssql container to be up / hack hackity hack hack
        call_command('create_db')
        call_command('migrate')
