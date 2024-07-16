from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def organizador(request):
    return render(request, 'organizador.html')

def academia(request):
    return render(request, 'academia.html')


def cadastro_academia(request):
    return render(request, 'cadastro_academia.html')
    
def academia_hub(request):
    return render(request, 'academia_hub.html')