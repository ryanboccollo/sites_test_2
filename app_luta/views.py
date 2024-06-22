from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def organizador(request):
    return render(request, 'organizador.html')

def academia(request):
    return render(request, 'academia.html')