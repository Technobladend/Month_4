from django.contrib import admin
from posts.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "rate", "created_at", "updated_at"]
    list_display_links = ["title", "content", "created_at", "updated_at"]
    list_filter = ['created_at', 'updated_at', 'category', 'tag']
    list_editable = ['rate']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]