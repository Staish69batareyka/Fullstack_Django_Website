from django.shortcuts import render

def index(request):
    return render(request, 'main/index/index.html')

def product_detail(request):
    pass