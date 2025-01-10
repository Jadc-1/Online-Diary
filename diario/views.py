from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoas

# Create your views here.
def home(request):
    return render(request, 'home.html')

def escrever(request):
    if request.method == 'GET':
        return render(request, 'escrever.html')
    elif request.method == 'POST':
        titulo = request.POST.get()
        tags = request.POST.getlist()
        pessoas = request.POST.getlist()
        texto = request.POST.get()
        return HttpResponse(F'{titulo} - {tags} - {pessoas} - {texto}')
    
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