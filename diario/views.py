from django.shortcuts import render
from django.http import HttpResponse

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
