from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post


def test_view(request):
    return HttpResponse("Hello World!")


def main_page_view(request):
    return render(request, 'base.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/post_detail.html', context={'post': post})