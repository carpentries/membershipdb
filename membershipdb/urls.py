#from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

from accounts import views as accounts_views
from membership import views as membership_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', membership_views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),

    path('organizations/', membership_views.organization_list, name='organization_list'),
    path('memberships/', membership_views.membership_list, name='membership_list'),
    path('contacts/', membership_views.contact_list, name='contact_list'),
    path('terms/', membership_views.term_list, name='term_list'),
    path('notes/', membership_views.note_list, name='note_list'),

    path('organization/<int:id>/', membership_views.organization_id, name='organization_id'),
    path('membership/<int:id>/', membership_views.membership_id, name='membership_id'),
    path('contact/<int:id>/', membership_views.contact_id, name='contact_id'),
    path('term/<int:id>/', membership_views.term_id, name='term_id'),
    path('note/<int:id>/', membership_views.note_id, name='note_id'),

    #path(r'^organization/(?P<id>\d+)/organization_form/$', membership_views.organization_form, name='organization_form'),
    #path(r'^organization_edit/(?P<id>\d+)/$', membership_views.organization_edit, name='organization_edit'),
    path('membership_edit/<int:id>/', membership_views.membership_edit, name='membership_edit'),
    #path(r'^contact_edit/(?P<id>\d+)/$', membership_views.contact_edit, name='contact_edit'),
]

