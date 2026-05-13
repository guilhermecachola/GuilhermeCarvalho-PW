from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Tecnologia, Competencia, Formacao
from .forms import TecnologiaForm, CompetenciaForm, FormacaoForm
from .models import Tecnologia, Competencia, Formacao, MakingOf, TipoTecnologia

def e_gestor(user):
    return user.is_superuser or user.groups.filter(name='gestor-portfolio').exists()
# --- LISTAGENS ---

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

# --- CRUD TECNOLOGIA ---

@login_required
@user_passes_test(e_gestor)
def nova_tecnologia(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@login_required
@user_passes_test(e_gestor)
def edita_tecnologia(request, id):
    obj = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Tecnologia'})

@login_required
@user_passes_test(e_gestor)
def apaga_tecnologia(request, id):
    obj = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/confirm_delete.html', {'objeto': obj, 'tipo': 'Tecnologia'})

# --- CRUD COMPETÊNCIA ---

@login_required
@user_passes_test(e_gestor)
def nova_competencia(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Competência'})

@login_required
@user_passes_test(e_gestor)
def edita_competencia(request, id):
    obj = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Competência'})

# --- CRUD FORMAÇÃO ---

@login_required
@user_passes_test(e_gestor)
def nova_formacao(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Formação'})

@login_required
@user_passes_test(e_gestor)
def edita_formacao(request, id):
    obj = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Formação'})

    from .models import Tecnologia, Competencia, Formacao, MakingOf, TipoTecnologia

def sobre_view(request):
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    makingof = MakingOf.objects.all().order_by('data')
    return render(request, 'portfolio/sobre.html', {
        'tipos': tipos,
        'makingof': makingof,
    })