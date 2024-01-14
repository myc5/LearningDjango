from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item
# Funcs that are called for specific views

def index(response):
    return HttpResponse("Root Page") #this also accepts HTML like <h1></h1>

def help_(response):
    return HttpResponse("Help Page")

def page1(response):
    return HttpResponse("<h1>Page 1</h1>")

#def db(response, id):
#    return HttpResponse(f"{id}") # ("%s" %id) also works

def todo(response, id):
    t_length = len(ToDoList.objects.all())
    object_list = []
    for i in range(t_length):
        obj = ToDoList.objects.all()[i].id
        object_list.append(obj)
    if id not in object_list:
        return HttpResponse(f"{id} does not exist (Try one of {object_list} instead.)")
    item = ToDoList.objects.get(id=id)
    return HttpResponse(f"{item.name}<br></br>Amount of ToDoLists: {t_length}")