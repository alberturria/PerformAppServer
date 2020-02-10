from common.utils.read_csv import read_csv_file
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self):
        read_csv_file('./../../data/basic_mdurance_1.csv')
