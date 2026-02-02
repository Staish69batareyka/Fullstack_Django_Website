from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1>Проверка связи</h1>')

def about(response):
    return HttpResponse('<h1>Это страница про нас</h1>')