from django, forms import fields
from django.contrib.suth.models import user
from django.contrib.auth.forms import UserCretionForm
from django import form

class UsuarioForm(UserCretionForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

        widgets = {
            'username': forms.TextInput(attrs=(
                'class': 'form-control'
            )),
            'email': forms.TextInput(attrs=(
                'class': 'form-control'
            )),
        }