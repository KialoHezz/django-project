from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # query certain or perticular object with id=1
    item = ls.item_set.get(id=1)

    return render(response, "main/list.html", {"ls":ls})
 
def home(response):
    return render(response, "main/home.html")


def create(response):
    return render(response, "main/create.html")