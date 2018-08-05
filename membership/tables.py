"""Membership tables
"""

import django_tables2 as tables
from .models import Organization, Membership, Contact, Term, Note
from django_tables2.utils import A

class OrganizationTable(tables.Table):
    name = tables.LinkColumn('organization_id', args=[A('id')])

    class Meta:
        model = Organization
        
        fields = ('name','country','url')
        template_name = 'django_tables2/bootstrap.html'


class MembershipTable(tables.Table):
    organization = tables.LinkColumn('membership_id', args=[A('id')])
    
    class Meta:
        model = Membership

        fields = ('organization','member_type','status')
        template_name = 'django_tables2/bootstrap.html'


class ContactTable(tables.Table):
    name = tables.LinkColumn('contact_id', args=[A('id')])
    last_name = tables.LinkColumn('contact_id', args=[A('id')])

    class Meta:
        model = Contact

        fields = ('name','last_name','organization','title')
        template_name = 'django_tables2/bootstrap.html'

