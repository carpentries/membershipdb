from django.contrib import admin

from .models import MembershipTerms, Organization, Person, Membership

admin.site.register(MembershipTerms)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Membership)
