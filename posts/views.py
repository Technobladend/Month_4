from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm2, CommentForm
from posts.models import Comment


def test_view(request):
    return HttpResponse("Hello!")


def main_page_view(request):
    return render(request, 'base.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = CommentForm()
        comments = post.comments.all()
        return render(
            request,
            'posts/post_detail.html',
            context={'post': post, 'form': form, 'comments': comments}
        )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'posts/post_detail.html',
                context={'post': post, 'form': form}
            )
        text = form.cleaned_data.get('text')
        Comment.objects.create(text=text, post=post)
        return redirect(f"/posts/{post_id}")


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, "posts/post_create.html", context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        form.save()
        return redirect("/posts/")