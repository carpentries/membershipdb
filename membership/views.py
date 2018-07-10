from django.shortcuts import render
from .models import Organization, Membership, Contact, Term, Note

def home(request):
    return render(request, 'home.html')

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})
    
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})    

def term_list(request):
    terms = Term.objects.all()
    return render(request, 'term_list.html', {'terms': terms})  

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes}) 

def organization_id(request, id):
    try:
        organization = Organization.objects.get(id=id)
        #import pdb; pdb.set_trace()
    except Organization.DoesNotExist:
        raise Http404
    return render(request, 'organization_id.html', {'organization_id': organization_id})


def membership_id(request, id):
    membership = Membership.objects.get(id=id)
    return render(request, 'membership_id.html', {'membership_id': membership_id})

def contact_id(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact_id.html', {'contact_id': contact_id})

def term_id(request, id):
    term = Term.objects.get(id=id)
    return render(request, 'term_id.html', {'term_id': term_id})

def note_id(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'note_id.html', {'note_id': note_id})