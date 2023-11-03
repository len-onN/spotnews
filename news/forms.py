from django import forms
from news.models import Category, User


class CreateCategoryForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Nome",
        widget=forms.TextInput(attrs={'type': 'text'})
    )


class CreateNewsForm(forms.Form):
    title = forms.CharField(
        label="Título"
    )
    content = forms.CharField(
        label="Conteúdo",
        widget=forms.Textarea
    )
    author = forms.ModelChoiceField(
        label="Autoria",
        queryset=User.objects.all()
    )
    created_at = forms.DateField(
        label="Criado em",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    image = forms.ImageField(
        label="URL da Imagem"
    )
    categories = forms.ModelMultipleChoiceField(
        label="Categorias",
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
