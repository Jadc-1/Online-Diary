from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoas, Diario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoas.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        if len(titulo.strip().lower()) == 0 or len(texto.strip()) == 0: ##Strip retira os espaços em brancos antes e depois, e o lower vai deixar todas as letras 
            return redirect('escrever')
            #TODO: Adicionar mensagens de erro

        diario = Diario(
            titulo = titulo,
            texto = texto,

        )
        diario.save()
        for i in pessoas:
            pessoa = Pessoas.objects.get(id = i)
            diario.pessoas.add(pessoa)

        diario.save()
        #TODO: Adicionar mensagens de sucesso
        return redirect('escrever')
    
def cadastrar_pessoa(request):
    if request.method == "GET":
        return render(request, 'pessoa.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        
        pessoa = Pessoas(
            nome = nome,
            foto = foto
        )
        pessoa.save()
        return redirect('escrever')