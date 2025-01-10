from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoas, Diario
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]
    return render(request, 'home.html', {'textos': textos})

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
        diario.set_tags(tags)
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
    ## Pegamos a data do proprio URL, então utilizamos GET, para pegar do url
def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada + timedelta(days=1)) ##o Banco de dados junto com datetime, trabalha com dias e horas, por isso temos que utilizar esse create_at__gte e __lte;

    return render(request, 'dia.html', {'diarios': diarios, 'total':diarios.count, 'data': data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia + timedelta(days=1))
    diarios.delete()
    return HttpResponse("delete")