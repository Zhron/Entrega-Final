from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
#from users.models import Imagen
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):

    return render(request, "AppEF/index.html")

def about(request):
    return render(request, 'AppEF/about.html')

@login_required
def about(request):
    return render(request, "AppEF/about.html")


