from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})

@login_required
def like_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.likes.filter(id=request.user.id).exists():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:lista')

@login_required
def novo_comentario(request, artigo_id):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, id=artigo_id)
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(artigo=artigo, autor=request.user, texto=texto)
    return redirect('artigos:lista')