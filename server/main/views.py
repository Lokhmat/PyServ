from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse


def homepage(request):
    return HttpResponse('Ok')
