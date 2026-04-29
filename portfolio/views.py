from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test  # Importes necessários
from .models import Tecnologia, Competencia, Formacao
from .forms import TecnologiaForm, CompetenciaForm, FormacaoForm

def e_gestor(user):
    """Retorna True se o utilizador estiver no grupo gestor-portfolio"""
    return user.groups.filter(name='gestor-portfolio').exists()


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