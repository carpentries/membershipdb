"""Membership forms module
"""
from django.forms import ModelForm
from .models import Note, Term


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
