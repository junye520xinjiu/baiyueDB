from django.shortcuts import render
from django.http.response import HttpResponse

def text(request,t):

    return HttpResponse(t)