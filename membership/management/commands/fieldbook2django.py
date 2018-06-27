"""
Move the data that was until june 13 in FieldBook to Django Data Model

Data used is private, this script is left public only for practical internal uses but
could be useful as an example for further projects.
"""

import csv
import datetime
from decimal import Decimal
from djmoney.money import Money
from django.core.management.base import BaseCommand
from membership.models import Term, Organization, Contact, Membership

def reverse_choices(choices):
    """
    Tuple of tuples -> Dict
    Returns a dictionary of reversed choices structures
    """
    return dict([(v, k) for k, v in choices])

MEMBERTYPE = reverse_choices(Term.TYPE_CHOICES)
STATUS = reverse_choices(Membership.STATUS_CHOICES)
NEWRENEW = reverse_choices(Membership.NEW_RENEW_CHOICES)
INVOICEREQUEST = reverse_choices(Membership.INVOICE_REQUEST)
EVENTSTATUS = reverse_choices(Membership.EVENT_STATUS)

def read_csv(filename):
    """
    Read values from csv filename and returns a list of OrderedDict for each row.
    """
    csv_data = []
    with open(filename, 'r') as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            csv_data.append(row)
    return csv_data

def to_bool(val):
    """
    str -> bool
    Convert "true"/"false" strings in corresponding Python boolean literals
    """
    return True if val == "true" else False

def add_terms(terms):
    """
    list of OrderedDict -> None
    Add MembershipTerms records in Fieldbook to MembershipDB Django Model
    """
    print("--- Start migrating Terms")
    for row in terms:
        Term.objects.update_or_create(
            mem_type=MEMBERTYPE[row["memtype"]],
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
    print("--- Finished migrating Terms")

def ifUKsetGB(country):
    """
    str -> str
    django-countries uses ISO 3166 for country codes, and GB is the UK's ISO 3166 country code.
    However, the .uk domain was created separately a few months before and .gb was never
    widely used and it is no longer possible to register under that domain.
    """
    return country if country != "UK" else "GB"

def add_orgs(orgs):
    """
    list of OrderedDict -> None
    Add Organizations records in Fieldbook to MembershipDB Django Model
    """
    print("--- Start migrating Organizations")
    for row in orgs:
        Organization.objects.update_or_create(
            shortname=row["shortname"],
            defaults={
                "name": row["partner"],
                "country": ifUKsetGB(row["Country"]),
                "domain": row["domain"],
                "umbrella": to_bool(row["umbrella"]),
                'vendor_reg': to_bool(row["Vendor Registration CI Completed"])
            }
        )
    print("--- Finished migrating Organizations")

def add_contacts(contacts):
    """
    list of OrderedDict -> None
    Add Persons records in Fieldbook to MembershipDB Django Model
    """
    print("--- Start migrating Contacts")
    for row in contacts:
        org = Organization.objects.get(domain=row["shortname"])
        name, last_name = row["partnercontact"].split()
        Contact.objects.update_or_create(
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
    print("--- Finished migrating Contacts")

def to_money(val):
    """
    str -> Money
    Convert string values to django-money entries
    """
    val = "$0" if val == '' else val
    val = val.split('$')[1].replace(',', '.')
    return Money(Decimal(val), 'USD')

def to_date(val):
    """
    str -> date
    Convert dd/mm/yyyy strings to datetime objects
    """
    return datetime.datetime.strptime(val, '%d/%m/%Y').date()

def add_memberships(memberships):
    """
    list of OrderedDict -> None
    Add Memberships records in Fieldbook to MembershipDB Django Model
    """
    print("--- Start migrating Memberships")
    for row in memberships:
        org = Organization.objects.get(domain=row["Name"])
        member_type = Term.objects.get(mem_type=MEMBERTYPE[row["type"]])
        Membership.objects.update_or_create(
            organization=org,
            start_date=to_date(row["startdate"]),
            defaults={
                "member_type": member_type,
                "status": STATUS.get(row["status"], ''),
                "new_renew": NEWRENEW.get(row["newrenew"], ''),
                "hubspot": row["HubSpot"],
                "annual_fee": to_money(row["annualfee"]),
                "paid_in_full": to_bool(row["Paid in Full"]),
                "expires": to_date(row["Expires"]),
                "agreement": row["agreement"],
                "invoice_request": INVOICEREQUEST.get(row["Invoice Request"], ''),
                "event_status": EVENTSTATUS.get(row["Event Status"], ''),
                "event": row["Event(s)"]
            }
        )
    print("--- Finished migrating Memberships")

class Command(BaseCommand):
    """
    fieldbook2django command to migrate data that was until june 13 in FieldBook to
    membershipdb Django Data Model
    """
    args = '<foo bar ...>'
    help = 'Populates the Django database with Fieldbook data'

    def handle(self, *args, **options):
        terms = read_csv("tmp/terms.csv")
        add_terms(terms)
        orgs = read_csv("tmp/organizations.csv")
        add_orgs(orgs)
        contacts = read_csv("tmp/persons.csv")
        add_contacts(contacts)
        memberships = read_csv("tmp/memberships.csv")
        add_memberships(memberships)



        



