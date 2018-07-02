from django.shortcuts import render
# from .models import Terms, Organization, Contact, Membership

def home(request):
    # title = nombre del modelo :Post..... .objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'membership/home.html', {})

    

