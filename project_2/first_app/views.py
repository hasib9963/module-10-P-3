from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('This is a home page')
    return render(request, 'first_app/home.html')
    
