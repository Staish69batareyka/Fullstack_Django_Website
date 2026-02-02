from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html') # Обращаемся к файлу из templates

def about(request):
    return render(request, 'main/about.html')