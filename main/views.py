from django.shortcuts import render
from django.http import HttpResponse

# Funcs that are called for specific views

def index(response):
    return HttpResponse("Root Page") #this also accepts HTML like <h1></h1>

def help_(response):
    return HttpResponse("Help Page")

def page1(response):
    return HttpResponse("<h1>Page 1</h1>")