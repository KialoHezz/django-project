from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # query certain or perticular object with id=1
    item = ls.item_set.get(id=1)

    return HttpResponse("<h1>%s</h1><br /><br /><p>%s</p>" %(ls.name, str(item.text)))