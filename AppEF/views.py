from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, SignUpForm, SearchForm
from .models import Post




def inicio(request):

    return render(request, "AppEF/index.html")

def about(request):
    return render(request, 'AppEF/about.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'AppEF/create_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'AppEF/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'AppEF/post_detail.html', {'post': post})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', post_id=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'AppEF/edit_post.html', {'form': form, 'post': post})
    else:
        return HttpResponseForbidden()

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        return render(request, 'AppEF/delete_post.html', {'post': post})
    else:
        return HttpResponseForbidden()


def search_posts(request):
    form = SearchForm(request.GET or None)
    posts = Post.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            posts = posts.filter(title__icontains=query)  # Search in titles; use __icontains for case-insensitive search

    return render(request, 'AppEF/post_list.html', {'posts': posts, 'form': form})