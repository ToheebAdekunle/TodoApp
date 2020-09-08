from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    feeds = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'feeds': feeds, 'form': form}
    return render(request, 'index.html', context)


def updateStuff(request, pk):
    stuff = Todo.objects.get(id=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=stuff)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = TodoForm(instance=stuff)

    context = {'form': form}

    return render(request, 'stuffs/update_stuff.html', context)


def deleteStuff(request, pk):
    stuff = Todo.objects.get(id=pk)

    if request.method == 'POST':
        stuff.delete()
        return redirect('/')

    context = {'stuff': stuff}

    return render(request, 'stuffs/delete_stuff.html', context)