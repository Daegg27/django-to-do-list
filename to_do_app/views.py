import re
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'to_do_app/index.html')

def signup_form(request):
    

    return render(request, 'to_do_app/signup_form.html')