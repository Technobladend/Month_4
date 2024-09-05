from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("Wassup")


def main_page_view(request):
    return render(request, 'base.html')