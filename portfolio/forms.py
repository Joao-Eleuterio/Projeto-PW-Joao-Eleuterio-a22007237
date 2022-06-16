from django.forms import ModelForm
from django import forms
from .models import Quizz, Projetos, Licenciatura, Cadeira, Noticia, Post, TFC


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
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

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome'}),
        }
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

        labels = {
            'Nome do projeto': 'Insira o nome do seu projeto',

            'imagem': 'Insira uma foto do seu projeto (200 x height)',

            'imagemGrande': 'Insira uma foto grande(pode ser a mesma) do seu projeto (500 x height)',

            'gif': 'Insira um gif da utilização do projeto',

            'descricao': 'Insira a descrição do projeto',

            'cadeira': 'Qual a cadeira pertecente ao projeto',

            'ano_realizacao': 'Indique o ano de realização do projeto',

            'participantes': 'Participantes:',

            'link_github': 'Link do GitHub do projeto',

            'Linguagens': 'Linguagens utilizadas no projeto',

            'Download': 'Projeto para download',
        }

        help_texts = {

        }


class LicenciaturaForm(ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'

        widgets = {
            'semestre': forms.NumberInput(attrs={'class': 'form-control', 'max': 2, 'min': 1}),
        }

        labels = {
            'Ano da faculdade': 'Ano da faculdade',
            'Semestre': 'Semestre da cadeira',
            'Cadeira': 'Cadeira',
            'Formação': 'formacao'
        }

        help_texts = {
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
            'ects': forms.NumberInput(attrs={'class': 'form-control', 'max': 20, 'min': 1}),
            'ranking': forms.NumberInput(attrs={'class': 'form-control', 'max': 5, 'min': 0}),
        }

        labels = {

        }

        help_texts = {
        }


class FormacaoForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        labels = {

        }

        help_texts = {
        }


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link': 'Link',
            'imagem': 'Imagem'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }


class TFCForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'

    labels = {
        'autores': 'Autor',
        'orientadores': 'Orientadores',
        'titulo': 'Titulo',
        'resumo': 'Resumo',
        'imagem': 'Imagem',
        'relatorio': 'Relatório',
        'github': 'GitHub',
        'video_demonstrativo': 'Video Demonstrativo',
    }
