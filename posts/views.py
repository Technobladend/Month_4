from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post, Tag, Comment
from posts.forms import PostForm2, CommentForm, SearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView

import user

def test_view(request):
    return HttpResponse(f"Hello!")


class TestView(View):
    def get(self, request):
        return HttpResponse("hello world")



def main_page_view(request):
    return render(request, 'base.html')


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

@login_required(login_url='login')
def post_list_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        posts = Post.objects.all()
        search = request.GET.get('search')
        tag = request.GET.getlist('tag')
        ordering = request.GET.get('ordering')

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        if tag:
            posts = posts.filter(tag__id__in=tag)

        if ordering:
            posts = posts.order_by(ordering)

        page = request.GET.get('page', 1)
        page = int(page)
        limit = 4
        total_posts = posts.count()
        max_pages = (total_posts + limit - 1) // limit

        if page < 1:
            page = 1
        elif page > max_pages:
            page = max_pages
        start = (page - 1) * limit
        end = start + limit

        posts = posts[start:end]

        context = {
            'posts': posts,
            'form': form,
            'max_pages': range(1, max_pages + 1),
        }

        return render(request, 'posts/post_list.html', context=context)

    



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
        return redirect(f"/api/v1/posts/posts/{post_id}")

@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, "posts/post_create.html", context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        form.save()
        return redirect("/api/v1/posts/posts")
    

@login_required(login_url='login')
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(request, 'posts/post_update.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', context={'form': form})
        form.save()
        return redirect("api/v1/user/profile")
    

