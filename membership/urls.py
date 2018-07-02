from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home),

    # url(r'^organizations/', include([
    #     url(r'^$', views.AllOrganizations.as_view(), name='all_organizations'),
    #     url(r'^add/$', views.OrganizationCreate.as_view(), name='organization_add'),
    # ])),
    # url(r'^organization/(?P<organization_id>[\w\.-]+)/', include([
    #     url(r'^$', views.OrganizationDetails.as_view(), name='organization_details'),
    #     url(r'^edit/$', views.OrganizationUpdate.as_view(), name='organization_edit'),
    #     url(r'^delete/$', views.OrganizationDelete.as_view(), name='organization_delete'),
    # ])),

    # url(r'^memberships/', include([
    #     url(r'^$', views.AllMemberships.as_view(), name='all_memberships'),
    #     url(r'^add/$', views.MembershipCreate.as_view(), name='membership_add'),
    # ])),
    # url(r'^membership/(?P<membership_id>\d+)/', include([
    #     url(r'^$', views.MembershipDetails.as_view(), name='membership_details'),
    #     url(r'^edit/$', views.MembershipUpdate.as_view(), name='membership_edit'),
    #     url(r'^delete/$', views.MembershipDelete.as_view(), name='membership_delete'),
    # ])),

    # url(r'^terms/', include([
    #     url(r'^$', views.AllTerms.as_view(), name='all_terms'),
    #     url(r'^add/$', views.TermsCreate.as_view(), name='terms_add'),
    # ])),
    # url(r'^term/(?P<term_id>\w+)/', include([
    #     url(r'^$', views.TermsDetails.as_view(), name='term_details'),
    #     url(r'^edit/$', views.TermtUpdate.as_view(), name='term_edit'),
    #     url(r'^delete/$', views.TermDelete.as_view(), name='term_delete'),
    # ])),

    # url(r'^contacts/', include([
    #     url(r'^$', views.AllContacts.as_view(), name='all_contacts'),
    #     url(r'^add/$', views.ContactCreate.as_view(), name='contacts_add'),
    # ])),
    # url(r'^contact/(?P<contact_id>\d+)/', include([
    #     url(r'^$', views.ContactDetails.as_view(), name='contact_details'),
    #     url(r'^edit/$', views.ContactUpdate.as_view(), name='contact_edit'),
    #     url(r'^delete/$', views.ContactDelete.as_view(), name='contact_delete'),
    # ])),

    # url(r'^notes/$', views.AllNotes.as_view(), name='all_notes'),
    # url(r'^note/(?P<note_id>\d+)/', include([
    #     url(r'^$', views.NoteDetails.as_view(), name='note_details'),
    #     url(r'^edit/$', views.NotetUpdate.as_view(), name='note_edit'),
    # ])),

]

  