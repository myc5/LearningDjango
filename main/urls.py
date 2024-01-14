# This file *inside* the app folder (different from the Django folder which also has this)
# defines how the URLs are resolved

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # "" is the root, views.index the normal func call name which it redirects to if the user types "" after the IP/site name (in this case, the root page)
    path("help", views.help_, name="help"),
    path("page1", views.page1, name="Page 1"),
    #path("<int:id>", views.db, name="Database"),
    path("<int:id>", views.todo, name="ToDo")
    ]