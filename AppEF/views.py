from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

def inicio(request):

    return render(request, "AppEF/index.html")

def about(request):
    return render(request, 'AppEF/about.html')