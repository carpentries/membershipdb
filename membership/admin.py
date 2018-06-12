from django.contrib import admin

from .models import MembershipTerm, Organization, Person, Membership

admin.site.register(MembershipTerm)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Membership)
