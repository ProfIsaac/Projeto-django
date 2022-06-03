from django.shortcuts import render
from core.models import Aluno

# Create your views here.
def home(request):  
    alunos = Aluno.objects.all() 
    return render(request, 'index.html', {'alunos':alunos})

    
def sobre(request):
    return render(request, 'sobre.html')






def contato(request):
    return render(request, 'contato.html')