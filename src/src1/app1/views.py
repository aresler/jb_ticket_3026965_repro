from django.shortcuts import render
from django.http import HttpResponse
from app2.models import func1

# Create your views here.

def index(request):
    return HttpResponse(func1())
