import re
from urllib import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
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

        things_to_do = Todo.objects.all()

        my_data = {
            'things_to_do':things_to_do
        }


        return render(request, 'to_do_app/index.html', my_data)

def signup_form(request):
    

    return render(request, 'to_do_app/signup_form.html')

def describe_task(request, id):
    
    task = Todo.objects.get(id = id)

    my_data = {
        'task': task
    }
    

    return render(request, 'to_do_app/describe_task.html', my_data)

def edit_task(request, id):

    task = Todo.objects.get(id = id)
    
    my_data = {
        'task': task
    }

    return render(request, 'to_do_app/edit_task.html', my_data)

def update_task(request):
    
    
    title = request.GET.get('title')
    description = request.GET.get('description')
    id = request.GET.get('id')

    task = Todo.objects.get(id = id)
    
    task.title = title
    task.description = description

    task.save()

    return JsonResponse({'title': title})
    # return HttpResponseRedirect('/todos') Cannot get this to work