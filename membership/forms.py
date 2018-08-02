"""Membership forms module
"""
from django.forms import ModelForm
from .models import Note, Term, Organization, Contact, Membership


class NoteForm(ModelForm):
    """Note Form
    """
    class Meta:
        model = Note
        fields = ['title', 'content', 'date_time']


class TermForm(ModelForm):
    """Term Form
    """
    class Meta:
        model = Term
        fields = ['mem_type', 'n_workshops',
                  'n_instructors', 'reserve',
                  'inh_trainer', 'local_train',
                  'publicize', 'recruit',
                  'coordinate']


class OrganizationForm(ModelForm):
    """Organization Form
    """
    class Meta:
        model = Organization
        fields = []


class ContactForm(ModelForm):
    """Contact Form
    """
    class Meta:
        model = Contact
        fields = []


class MembershipForm(ModelForm):
    """Membership Form
    """
    class Meta:
        model = Membership
        fields = []

