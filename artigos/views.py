from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario, Rating


def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    e_blogger = request.user.is_authenticated and request.user.groups.filter(name='bloggers').exists()
    return render(request, 'artigos/lista.html', {'artigos': artigos, 'e_blogger': e_blogger})


def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'artigos/detalhe.html', {'artigo': artigo})


@login_required
def novo_artigo(request):
    if request.method == 'POST':
        titulo   = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        link     = request.POST.get('link_externo')
        imagem   = request.FILES.get('imagem')
        Artigo.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            link_externo=link or None,
            imagem=imagem,
            autor=request.user
        )
        return redirect('artigos:lista')
    return render(request, 'artigos/novo_artigo.html')


def novo_comentario(request, artigo_id):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, id=artigo_id)
        autor  = request.POST.get('autor', 'Anónimo')
        texto  = request.POST.get('texto')
        if texto:
            Comentario.objects.create(artigo=artigo, autor=autor, texto=texto)
    return redirect('artigos:detalhe', artigo_id=artigo_id)


def rating_artigo(request, artigo_id):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, id=artigo_id)
        valor  = int(request.POST.get('valor', 3))
        ip     = request.META.get('REMOTE_ADDR')
        Rating.objects.update_or_create(
            artigo=artigo, ip=ip,
            defaults={'valor': valor}
        )
    return redirect('artigos:detalhe', artigo_id=artigo_id)