from django import forms
from parser.models import TVParser
from parser.parser import parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("FILMS", "FILMS"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ["media_type"]

    def parser_data(self):
        if self.data["media_type"] == "FILMS":
            film_parser = parser()
            items_to_create = []
            for i in film_parser:
                post = TVParser(**i)
                items_to_create.append(post)

            TVParser.objects.bulk_create(items_to_create)