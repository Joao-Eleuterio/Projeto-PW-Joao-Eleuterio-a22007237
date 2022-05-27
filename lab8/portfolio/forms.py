from django.forms import ModelForm
from django import forms
from .models import Post, Quizz, Projetos, Licenciatura, Cadeira


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do post...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),

        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',

        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': ' prioridade: baixa=1, media=2, alta=3',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        labels = {

            'nome': 'Qual o seu nome?',

            'pergunta1': 'O que é HTML?',  # O que é HTML? (linguagem de marcação)

            'pergunta2': 'O que é o Django?',  # O que é o Django? (framework)

            'pergunta3': 'Em que ano foi criado o Django? ',  # Em que ano foi criado o Django? (2005)

            'pergunta4': 'Em que ano foi criado o CSS',  # Em que ano foi criado o CSS (1994)

            'pergunta5': 'O que significa CSS',  # O que significa CSS (cascading style sheet)

        }

        help_texts = {
            'pergunta1': '(escreva em minusculas)',
            'pergunta2': '(escreva em minusculas)',
            'pergunta5': '(escreva em minusculas)',
        }


class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'

        widgets = {
        }

        labels = {

            'imagem': 'Insira uma foto do seu projeto',

            'descricao': 'Insira a descrição do projeto',

            'cadeira': 'Qual a cadeira pertecente ao projeto',

            'ano_realizacao': 'Indique o ano de realização do projeto',

            'participantes': 'Participantes:',

            'link_github': 'Link do GitHub do projeto',
        }

        help_texts = {
        }


class LicenciaturaForm(ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'

        widgets = {
        }

        labels = {

        }

        help_texts = {
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
        }

        labels = {

        }

        help_texts = {
        }


class FormacaoForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
        }

        labels = {

        }

        help_texts = {
        }
