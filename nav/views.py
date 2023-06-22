from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # query certain or perticular object with id=1
    # item = ls.item_set.get(id=1)

    return render(response, "main/list.html", {"ls":ls})
 
def home(response):
    return render(response, "main/home.html")


def create(response):
    # instantiate
    if response.method == "POST":
        form = CreateNewList(response.POST)
        # validate
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        # to redirect to new ToDoList
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})