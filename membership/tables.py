"""Membership tables
"""

import django_tables2 as tables
from .models import Organization, Membership, Contact, Term, Note
from django_tables2.utils import A

class OrganizationTable(tables.Table):
    class Meta:
        model = Organization
        fields = ('name','country','url')
        name = tables.LinkColumn('organization_id', args=[A('pk')])
        template_name = 'django_tables2/bootstrap.html'
