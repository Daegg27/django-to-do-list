import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from .models import *

# Create your views here.

@csrf_exempt
def index(request):

    if request.method == 'POST': 
        body = json.loads(request.body)
        title = body['title']
        description = body['description']

        new_task = Todo(title = title, description = description)
        new_task.save()
        return JsonResponse(model_to_dict(new_task))


    else:
        return render(request, 'to_do_app/index.html')

def signup_form(request):
    

    return render(request, 'to_do_app/signup_form.html')