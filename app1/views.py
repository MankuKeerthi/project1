from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def keerthi(request):
    return HttpResponse('<h1><marquee>Keerthi is a good girl</marquee></h1>')
