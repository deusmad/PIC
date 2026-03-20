from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        'Привет, Мир!',
        content_type="text/plain; charset=utf-8"
    )


def hello(request):
    return HttpResponse(
        'Привет, Мир!'
    )
