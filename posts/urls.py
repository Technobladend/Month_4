from django.urls import path
from posts.views import (
    post_list_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    PostListView,
)

urlpatterns = [
    path('posts/', post_list_view, name='post_list'),
    path('posts2/', PostListView.as_view(), name='post_list2'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view, name='post_create'),
    path('posts/<int:post_id>/update/', post_update_view, name='post_update'),
]
