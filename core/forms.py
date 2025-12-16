from django import forms
from .models import ContactMessage, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )

    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Escribí tu mensaje...'
        })
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="Máximo 150 caracteres. Letras, números y @/./+/-/_ únicamente."
    )

    email = forms.EmailField(
        label="Correo electrónico"
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="""
        <ul>
            <li>No puede ser similar a tu información personal.</li>
            <li>Debe tener al menos 8 caracteres.</li>
            <li>No puede ser una contraseña común.</li>
            <li>No puede ser solo numérica.</li>
        </ul>
        """
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text="Ingresá la misma contraseña para verificación."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'category': 'Categoría',
            'image': 'Imagen',
        }
