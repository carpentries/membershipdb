"""
Move the data that was until june 13 in FieldBook to Django Data Model

Data used is private, this script is left public only for practical internal uses but
could be useful as an example for further projects.
"""

import csv

from django.core.management.base import BaseCommand, CommandError
from membership.models import Term

dmemtype = dict([(v, k) for k, v in Term.TYPE_CHOICES])

def read_csv(filename):
    csv_data = []
    with open(filename, 'r') as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            csv_data.append(row)
    return csv_data

def add_terms(terms):
    def to_bool(val):
        return True if val == "true" else False

    for row in terms:
        term, created = Term.objects.update_or_create(
            mem_type=dmemtype[row["memtype"]],
            defaults={
                "n_workshops": int(row["numorgworkshops"]),
                "n_instructors": int(row["instructors"]),
                "reserve": to_bool(row["reserve"]),
                "inh_trainer": to_bool(row["inhousetrainer"]),
                "local_train": to_bool(row["localtrain"]),
                "publicize": to_bool(row["publicize"]),
                "recruit": to_bool(row["recruit"]),
                "coordinate": to_bool(row["coordinate"])
            }
        )
        

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Populates the Django database with Fieldbook data'

    def handle(self, *args, **options):
        terms = read_csv("tmp/terms.csv")
        add_terms(terms)



        



