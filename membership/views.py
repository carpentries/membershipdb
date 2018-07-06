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