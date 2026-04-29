from django.contrib.auth.models import Group

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Garante que o utilizador entra no grupo de autores
            grupo, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            
            login(request, user)
            return redirect('portfolio:tecnologias')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})