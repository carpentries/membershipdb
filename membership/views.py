from django.shortcuts import render, get_object_or_404
from .models import Organization, Membership, Contact, Term, Note

def home(request):
    return render(request, 'home.html')

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships},)
    
def contact_list(request):
    contacts = Contact.objects.all()
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
    organizations = Organization.objects.all()
    return render(request, 'organization_edit.html', {'organizations': organizations})

def membership_edit(request, id):
    d_status_type = dict(Membership.STATUS_CHOICES)
    memberships = Membership.objects.all()
    return render(request, 'membership_edit.html', {'memberships': memberships, 'status_type': d_status_type})

def contact_edit(request, id):
    contacts = Contact.objects.all()
    return render(request, 'contact_edit.html', {'contacts': contacts})

def organization_form(request, id):
    organization = get_object_or_404(Organization, id=id)
    return render(request, 'organization_form.html', {'organization': organization})
