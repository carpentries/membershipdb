from django.contrib import admin

from .models import Note, MembershipTerm, Organization, Person, Membership

admin.site.register(Note)
admin.site.register(MembershipTerm)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Membership)
