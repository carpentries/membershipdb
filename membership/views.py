from django.shortcuts import render, get_object_or_404
from .models import Organization, Membership, Contact, Term, Note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'landing.html')

def organization_list(request):
    organizations_list = Organization.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(organizations_list, 10)
    try:
        organizations = paginator.page(page)
    except PageNotAnInteger:
        organizations = paginator.page(1)
    except EmptyPage:
        organizations = paginator.page(paginator.num_pages)

    return render(request, 'organization_list.html', {'organizations': organizations})

def membership_list(request):
    memberships_list = Membership.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(memberships_list, 10)
    try:
        memberships = paginator.page(page)
    except PageNotAnInteger:
        memberships = paginator.page(1)
    except EmptyPage:
        memberships = paginator.page(paginator.num_pages)

    return render(request, 'membership_list.html', {'memberships': memberships},)
    
def contact_list(request):
    contacts_list = Contact.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(contacts_list, 10)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'contact_list.html', {'contacts': contacts})    

def term_list(request):
    d_term_type = dict(Term.TYPE_CHOICES)
    terms = Term.objects.all()
    for term in terms:
        term.mem_type = d_term_type[term.mem_type]
    return render(request, 'term_list.html', {'terms': terms})  

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes}) 

def organization_id(request, id):
    try:
        organization = Organization.objects.get(id=id)
    except Organization.DoesNotExist:
        raise Http404
    return render(request, 'organization_id.html', {'organization': organization})

def membership_id(request, id):
    try:
        membership = Membership.objects.get(id=id)
    except Membership.DoesNotExist:
        raise Http404    
    return render(request, 'membership_id.html', {'membership': membership})

def contact_id(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact_id.html', {'contact': contact})

def term_id(request, id):
    term = Term.objects.get(id=id)
    return render(request, 'term_id.html', {'term': term})

def note_id(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'note_id.html', {'note': note})

def organization_edit(request, id):
    organization = Organization.objects.get(id=id)
    return render(request, 'organization_edit.html', {'organization': organization})

def membership_edit(request, id):
    d_status_type = dict(Membership.STATUS_CHOICES)
    d_new_renew = dict(Membership.NEW_RENEW_CHOICES)
    membership = Membership.objects.get(id=id)
    return render(request, 'membership_edit.html', {'membership': membership, 'status_type': d_status_type, 'new_renew': d_new_renew})

def contact_edit(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact_edit.html', {'contact': contact})

def term_edit(request, id):
    term = Term.objects.get(id=id)
    return render(request, 'term_edit.html', {'term': term})

def organization_form(request, id):
    organization = get_object_or_404(Organization, id=id)
    return render(request, 'organization_form.html', {'organization': organization})
