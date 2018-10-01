from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render('',{})
    return render(request, 'mainsite/index.html')

def about(request):
    return render(request, 'mainsite/contact.html')

def services(request):
     return render(request, 'mainsite/services.html')
    
