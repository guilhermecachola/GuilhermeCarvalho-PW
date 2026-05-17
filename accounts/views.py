from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import RegistoForm

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('portfolio:home')
        else:
            erro = 'Utilizador ou password incorretos.'
    return render(request, 'accounts/login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('portfolio:home')

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, _ = Group.objects.get_or_create(name='bloggers')
            user.groups.add(grupo)
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})