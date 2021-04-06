from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse


def homepage(request):
    return HttpResponse('Ok')

def index(request):
    return render(request, 'main/index.html')