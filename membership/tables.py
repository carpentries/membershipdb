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
        order_by = ('name')
        template_name = 'django_tables2/bootstrap.html'


class MembershipTable(tables.Table):
    organization = tables.LinkColumn('membership_id', args=[A('id')])
    
    class Meta:
        model = Membership
        fields = ('organization','member_type','status')
        order_by = ('organization')
        template_name = 'django_tables2/bootstrap.html'


class ContactTable(tables.Table):
    name = tables.LinkColumn('contact_id', args=[A('id')])
    last_name = tables.LinkColumn('contact_id', args=[A('id')])

    class Meta:
        model = Contact
        fields = ('name','last_name','organization','title')
        order_by = ('name','last_name','organization')
        template_name = 'django_tables2/bootstrap.html'


class TermTable(tables.Table):
    mem_type = tables.LinkColumn('term_id', args=[A('id')])

    class Meta:
        model = Term
        fields = ('mem_type','n_workshops')
        order_by = ('mem_type')
        template_name = 'django_tables2/bootstrap.html'


class NoteTable(tables.Table):
    title = tables.LinkColumn('note_id', args=[A('id')])

    class Meta:
        model = Note
        fields = ('title','content','date_time')
        order_by = ('title','date_time')



