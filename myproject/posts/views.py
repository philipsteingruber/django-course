from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Post


def posts_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request: HttpRequest, slug: str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})
