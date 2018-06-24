"""
Move the data that was until june 13 in FieldBook to Django Data Model

Data used is private, this script is left public only for practical internal uses but
could be useful as an example for further projects.
"""

import csv

from django.core.management.base import BaseCommand, CommandError
from membership.models import Term, Organization, Contact

dmemtype = dict([(v, k) for k, v in Term.TYPE_CHOICES])

def read_csv(filename):
    csv_data = []
    with open(filename, 'r') as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            csv_data.append(row)
    return csv_data

def to_bool(val):
    return True if val == "true" else False

def add_terms(terms):
    for row in terms:
        term, updated = Term.objects.update_or_create(
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

def ifUKsetGB(country):
    return country if country != "UK" else "GB"

def add_orgs(orgs):
    for row in orgs:
        org, updated = Organization.objects.update_or_create(
            shortname=row["shortname"],
            defaults={
                "name": row["partner"],
                "country": ifUKsetGB(row["Country"]),
                "domain": row["domain"],
                "umbrella": to_bool(row["umbrella"]),
                'vendor_reg': to_bool(row["Vendor Registration CI Completed"])
            }
        )

def add_contacts(contacts):
    for row in contacts:
        org = Organization.objects.get(domain=row["shortname"])
        name, last_name=row["partnercontact"].split()
        contact, updated = Contact.objects.update_or_create(
            name=name,
            last_name=last_name,
            defaults={
                "organization": org,
                "title": row["title"],
                "email": row["partneremail"],
                "advisory_council": to_bool(row["Advisory Council"]),
                "signatory": to_bool(row["Signatory"]),
                "member_contact": to_bool(row["Member Contact"]),
                "billing_contact": to_bool(row["Billing Contact"]),
                "trainer": to_bool(row["Instructor Trainer"]),
                "merger_notify": to_bool(row["MergerNotify"]),
                "nf2nci_letter": to_bool(row["NF2CIAssignment"]),
                "hubspot": row["HubSpot"],
                "address": row["Address"],
                "phone": row["partnerphone"]
            }
        )


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Populates the Django database with Fieldbook data'

    def handle(self, *args, **options):
        terms = read_csv("tmp/terms.csv")
        add_terms(terms)
        orgs = read_csv("tmp/organizations.csv")
        add_orgs(orgs)
        contacts = read_csv("tmp/persons.csv")
        add_contacts(contacts)



        



