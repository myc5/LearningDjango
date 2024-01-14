from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length = 200) #always add the max_length if using CharField
    
    def __str__(self):
        return self.name

class Item(models.Model):
    # add entries from ToDoList as FKs; cascade like in SQL means that children entries are deleted if parent entries are deleted
    # ToDoList here is an object
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text
    
""" This works but is not necessary right now

t = ToDoList(name="List 1")
t.save()
t.item_set.create(text="Do this thing 1", complete=False)
t.item_set.create(text="Do this thing 2", complete=True)
"""