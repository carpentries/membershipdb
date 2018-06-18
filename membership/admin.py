from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Note, Term, Organization, Person, Membership

class NoteInline(GenericTabularInline):
    model = Note
    max_num = 1

class TermAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class MembershipAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

admin.site.register(Note)
admin.site.register(Term, TermAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Membership, MembershipAdmin)
