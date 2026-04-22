from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnologia, Competencia, Formacao
from .forms import TecnologiaForm, CompetenciaForm, FormacaoForm


def nova_tecnologia(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def edita_tecnologia(request, id):
    obj = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def apaga_tecnologia(request, id):
    obj = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/confirm_delete.html', {'objeto': obj, 'tipo': 'Tecnologia'})

# --- CRUD COMPETÊNCIA ---
def nova_competencia(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Competência'})

def edita_competencia(request, id):
    obj = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Competência'})


def nova_formacao(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Formação'})

def edita_formacao(request, id):
    obj = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Formação'})