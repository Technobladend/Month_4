from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView

from parser.forms import ParserForm
from parser.models import TVParser


class FilmListView(ListView):
    model = TVParser
    template_name = 'parser/film_list.html'
    paginate_by = 5


    def get_queryset(self):
        return TVParser.objects.all()


class ParserView(FormView):
    template_name = 'parser/start_parsing.html'
    form_class = ParserForm

    def post(self, request, *args, **kwargs):
        form = ParserForm(request.POST)
        if not form.is_valid():
            return super(ParserView.post(*args, **kwargs))
        form.parser_data()
        return HttpResponse("OK")