from django.urls import path
from parser.views import ParserView, FilmListView


urlpatterns = [
    path('films/', FilmListView.as_view(), name='parser'),
    path('parsing/', ParserView.as_view(), name='parser'),

]