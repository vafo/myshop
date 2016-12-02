from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("News")


def news(request, news):
    return HttpResponse(''.join(["News ID #", news]))
