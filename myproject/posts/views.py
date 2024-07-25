from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms
from .models import Post


def posts_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request: HttpRequest, slug: str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})


@login_required(login_url='/users/login/')
def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})
