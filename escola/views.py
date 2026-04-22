from django.shortcuts import render
from .models import Curso, Aluno  # Importe também o modelo Aluno

# A sua função atual (já está correta)
def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})

# Nova função para listar Alunos
def alunos_view(request):
    # 1. Procurar todos os alunos na base de dados
    alunos = Aluno.objects.all().order_by('nome')
    
    # 2. Criar o dicionário de contexto com os dados
    context = {
        'alunos': alunos,
        'titulo': 'Lista de Alunos Registados'
    }
    
    # 3. Renderizar o template enviando o contexto
    return render(request, 'escola/alunos.html', context)