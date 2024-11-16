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

def login(request):
    return render(request, 'login.html')

def cadastrar_lutador(request):
    if request.method == 'POST':
        form = LutadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_lutadores')  # Redireciona para a lista de lutadores
    else:
        form = LutadorForm()
    return render(request, 'cadastro_lutador.html', {'form': form})

# View para listar os lutadores cadastrados
def listar_lutadores(request):
    lutadores = Lutador.objects.all()
    return render(request, 'listar_lutadores.html', {'lutadores': lutadores})