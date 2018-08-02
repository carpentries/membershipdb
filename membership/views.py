"""Membership views
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django_tables2 import RequestConfig

from .models import Organization, Membership, Contact, Term, Note
from .forms import TermForm
from .tables import OrganizationTable


def home(request):
    """Home and landing view
    """
    if request.user.is_authenticated:
        organizations = Organization.objects.all().count
        memberships = Membership.objects.all().count
        terms = Term.objects.all().count
        contacts = Contact.objects.all().count
        notes = Note.objects.all().count
        
        return render(request, 'home.html', {'organizations':organizations, 'memberships':memberships, 'terms':terms, 'contacts':contacts, 'notes':notes})
    else:
        return render(request, 'landing.html')


def organization_list(request):
    """Organizations list view
    """
    organizations = OrganizationTable(Organization.objects.all())
    RequestConfig(request).configure(organizations)    
    # organizations_list = Organization.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(organizations_list, 10)
    # try:
    #     organizations = paginator.page(page)
    # except PageNotAnInteger:
    #     organizations = paginator.page(1)
    # except EmptyPage:
    #     organizations = paginator.page(paginator.num_pages)

    return render(request, 'organization_list.html',
                  {'organizations': organizations})


def membership_list(request):
    """Memberships list view
    """
    memberships_list = Membership.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(memberships_list, 10)
    try:
        memberships = paginator.page(page)
    except PageNotAnInteger:
        memberships = paginator.page(1)
    except EmptyPage:
        memberships = paginator.page(paginator.num_pages)

    return render(request, 'membership_list.html',
                  {'memberships': memberships})


def contact_list(request):
    """Contacts list view
    """
    contacts_list = Contact.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(contacts_list, 10)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(
        request, 'contact_list.html',
        {'contacts': contacts})


def term_list(request):
    """Terms list view
    """
    d_term_type = dict(Term.TYPE_CHOICES)
    terms_list = Term.objects.all()
    for term in terms_list:
        term.mem_type = d_term_type[term.mem_type]

    page = request.GET.get('page', 1)

    paginator = Paginator(terms_list, 10)
    try:
        terms = paginator.page(page)
    except PageNotAnInteger:
        terms = paginator.page(1)
    except EmptyPage:
        terms = paginator.page(paginator.num_pages)

    return render(request, 'term_list.html', {'terms': terms})


def note_list(request):
    """Notes list view
    """
    notes_list = Note.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(notes_list, 10)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    return render(request, 'note_list.html', {'notes': notes})


def organization_id(request, org_id):
    """Organization detail view
    """
    try:
        organization = Organization.objects.get(id=org_id)
    except Organization.DoesNotExist:
        raise Http404("Organization does not exist")
    return render(request, 'organization_id.html',
                  {'organization': organization})


def membership_id(request, mmb_id):
    """Membership detail view
    """
    try:
        membership = Membership.objects.get(id=mmb_id)
    except Membership.DoesNotExist:
        raise Http404("Membership does not exist")
    return render(request, 'membership_id.html', {'membership': membership})


def contact_id(request, ctc_id):
    """Contact detail view
    """
    contact = Contact.objects.get(id=ctc_id)
    return render(request, 'contact_id.html', {'contact': contact})


def term_id(request, trm_id):
    """Term detail view
    """
    term = Term.objects.get(id=trm_id)
    return render(request, 'term_id.html', {'term': term})


def note_id(request, nt_id):
    """Note detail view
    """
    note = Note.objects.get(id=nt_id)
    return render(request, 'note_id.html', {'note': note})


def organization_edit(request, org_id):
    """Organization edit view
    """
    organization = Organization.objects.get(id=org_id)
    return render(request, 'organization_edit.html',
                  {'organization': organization})


def membership_edit(request, mmb_id):
    """Membership edit view
    """
    d_status_type = dict(Membership.STATUS_CHOICES)
    d_new_renew = dict(Membership.NEW_RENEW_CHOICES)
    membership = Membership.objects.get(id=mmb_id)
    return render(request, 'membership_edit.html',
                  {'membership': membership,
                   'status_type': d_status_type,
                   'new_renew': d_new_renew})


def contact_edit(request, ctc_id):
    """Contact edit view
    """
    contact = Contact.objects.get(id=ctc_id)
    return render(request, 'contact_edit.html', {'contact': contact})


def term_edit(request, trm_id):
    """Term edit view
    """
    post = get_object_or_404(Term, id=trm_id)
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = TermForm()
    return render(
        request, 'term_edit.html',
        {'post': post, 'form': form})


def organization_form(request, org_id):
    """Organization form view
    """
    organization = get_object_or_404(Organization, id=org_id)
    return render(request, 'organization_form.html',
                  {'organization': organization})
