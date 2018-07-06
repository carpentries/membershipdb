import re
from django.conf.urls import include, url
from django.contrib import admin

from accounts import views as accounts_views
from membership import views as membership_views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', membership_views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^organizations/$', membership_views.organization_list, name='organization_list'),
    url(r'^memberships/$', membership_views.membership_list, name='membership_list'),
    url(r'^contacts/$', membership_views.contact_list, name='contact_list'),
    url(r'^terms/$', membership_views.term_list, name='term_list'),
    url(r'^notes/$', membership_views.note_list, name='note_list'),
]

