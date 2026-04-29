from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistoForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório para contacto.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)