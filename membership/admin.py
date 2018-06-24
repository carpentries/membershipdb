from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Note, Term, Organization, Contact, Membership

class NoteInline(GenericTabularInline):
    model = Note
    max_num = 1

class OrgInline(admin.TabularInline):
    model = Organization
    max_num = 1

class ContactInline(admin.TabularInline):
    model = Contact
    max_num = 1

class TermAdmin(admin.ModelAdmin):
    list_display = (
        'mem_type', 'n_workshops', 'n_instructors',
        'reserve', 'inh_trainer', 'local_train',
        'publicize', 'recruit', 'coordinate'
        )
    inlines = [
        NoteInline,
    ]

class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'shortname', 'country',
        'domain', 'umbrella', 'vendor_reg'
        )    
    inlines = [
        ContactInline,
        NoteInline
    ]

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'organization', 'name', 'last_name',
        'title', 'email', 'advisory_council',
        'signatory', 'member_contact', 'billing_contact',
        'trainer', 'merger_notify', 'nf2nci_letter',
        'hubspot', 'address', 'phone'
        )  
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
admin.site.register(Contact, ContactAdmin)
admin.site.register(Membership, MembershipAdmin)
