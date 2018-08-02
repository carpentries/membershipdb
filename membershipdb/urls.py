"""MembershipDB project urls
"""

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from accounts import views as accounts_views
from membership import views as membership_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', membership_views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    path(
        'organizations/',
        membership_views.organization_list,
        name='organization_list'
        ),
    path(
        'memberships/',
        membership_views.membership_list,
        name='membership_list'
        ),
    path(
        'contacts/',
        membership_views.contact_list,
        name='contact_list'
        ),
    path(
        'terms/',
        membership_views.term_list,
        name='term_list'
        ),
    path(
        'notes/',
        membership_views.note_list,
        name='note_list'
        ),

    path(
        'organization/<int:org_id>/',
        membership_views.organization_id,
        name='organization_id'
        ),
    path(
        'membership/<int:mmb_id>/',
        membership_views.membership_id,
        name='membership_id'
        ),
    path(
        'contact/<int:ctc_id>/',
        membership_views.contact_id,
        name='contact_id'
        ),
    path(
        'term/<int:trm_id>/',
        membership_views.term_id,
        name='term_id'
        ),
    path(
        'note/<int:nt_id>/',
        membership_views.note_id,
        name='note_id'
        ),

    path(
        'organization_edit/<int:org_id>/',
        membership_views.organization_edit,
        name='organization_edit'
        ),
    path(
        'membership_edit/<int:mmb_id>/',
        membership_views.membership_edit,
        name='membership_edit'
        ),
    path(
        'contact_edit/<int:ctc_id>/',
        membership_views.contact_edit,
        name='contact_edit'
        ),
    path(
        'term_edit/<int:trm_id>/',
        membership_views.term_edit,
        name='term_edit'
        ),
    path(
        'note_edit/<int:nt_id>/',
        membership_views.note_edit,
        name='note_edit'
        ),
]
