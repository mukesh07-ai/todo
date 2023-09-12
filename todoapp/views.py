from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm


def index(request):
    if request.method == "POST":
        a = CreateUserForm(request.POST)
        if a.is_valid():
            a.save()
    a = CreateUserForm()
    b = todo.objects.all()
    return render(request, "index.html", {"form":a, "data":b})


def delete(request, id):
    c = todo.objects.get(id=id)
    c.delete()
    return redirect("index")
    

# Create your views here.
