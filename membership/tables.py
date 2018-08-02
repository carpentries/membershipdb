"""Membership tables
"""

import django_tables2 as tables
from .models import Organization, Membership, Contact, Term, Note

class OrganizationTable(tables.Table):
    class Meta:
        model = Organization
        fields = ('name','country','url')
        template_name = 'django_tables2/table.html'
