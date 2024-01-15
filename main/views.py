from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import ToDoList, Item
from .forms import CreateForm

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
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
    
    if response.method == "POST": # Dict {"save": ["save"], "c1": ["clicked"]} - these are the values set in todo.html
        print(response.POST)    
        if response.POST.get("save"):
            for tasks in item.item_set.all():
                if response.POST.get("c" + str(tasks.id)) == "clicked":
                    tasks.complete = True
                else:
                    tasks.complete = False
                tasks.save() 
        elif response.POST.get("newItem"):    
            txt = response.POST.get("new")
            if len(txt) >= 3:
                item.item_set.create(text=txt, complete=False)    
            else:
                print("Input too short")    
        
    return render(response, "main/todo.html", {"result": "It worked", "item": item, "t_length": t_length})

def create(response):
    if response.method == "POST": # check which request type we are using, the default is GET
        form = CreateForm(response.POST)        
        if form.is_valid(): # the .is_valid method checks if all required fields were filled in correctly
            n = form.cleaned_data["name"] # extract the clear type name and save it in our ToDoList
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect(f"/{t.id}") # Once saved, redirect to the new list immediately
    else:
        form = CreateForm()    
    return render(response, "main/create.html", {"form":form})

@login_required(login_url= "/admin")
def debug(response):
    todo_lists = ToDoList.objects.all()
    t_length = len(ToDoList.objects.all())
    object_dict = {}
    for i in range(t_length):
        obj = ToDoList.objects.all()[i].id
        object_dict[f"id={obj}"] = ToDoList.objects.get(id=obj)
    return render(response, "main/debug.html", {"todo_lists": todo_lists, "todo_length": t_length, "todo_dict": object_dict})

# Trying out a classed-based view
class ToDoListView(ListView):
    model = ToDoList # Model name goes here
    context_object_name = "todo_lists" # context names like in the return render go here
    template_name = "main/list.html" # as above
