from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item
from .forms import CreateForm
# Funcs that are called for specific views

"""def home(response):
    return HttpResponse("Home Page") #this also accepts HTML like <h1></h1>"""

# Using our self-written HTML page here
def home(response):
    page_name = "Home Page"
    return render(response, "main/home.html", {})

def help_(response):
    page_name = "Help Page"
    return render(response, "main/help.html", {})

def page1(response):
    return HttpResponse("<h1>Page 1</h1>")

#def db(response, id):
#    return HttpResponse(f"{id}") # ("%s" %id) also works

# Old version without template
"""
def todo(response, id):
    t_length = len(ToDoList.objects.all())
    object_list = []
    for i in range(t_length):
        obj = ToDoList.objects.all()[i].id
        object_list.append(obj)
    if id not in object_list:
        return HttpResponse(f"{id} does not exist (Try one of {object_list} instead.)")
    item = ToDoList.objects.get(id=id)
    return HttpResponse(f"{item.name}<br></br>Amount of ToDoLists: {t_length}")"""

# New version with template and offloaded if/else checks   
def todo(response, id):
    t_length = len(ToDoList.objects.all())
    object_list = []
    for i in range(t_length):
        obj = ToDoList.objects.all()[i].id
        object_list.append(obj)
    if id not in object_list:
        return render(response, "main/todo.html", {"result": "Error", "id": id, "object_list": object_list})
    item = ToDoList.objects.get(id=id)
    return render(response, "main/todo.html", {"result": "It worked", "item": item, "t_length": t_length})

def create(response):
    form = CreateForm()    
    return render(response, "main/create.html", {"form":form})