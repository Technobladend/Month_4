from django.contrib import admin
from parser.models import TVParser


@admin.register(TVParser)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('title_name', 'title_url', 'image')
    search_fields = ['title_name']