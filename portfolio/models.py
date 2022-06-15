# Create your models here.
import datetime

from django.db import models


def resolution_path(instance, filename):
    return f'noticia/{instance.id}'


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.autor}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)
    pergunta1 = models.CharField(max_length=50)  # O que é HTML? (linguagem de marcação)
    pergunta2 = models.CharField(max_length=50)  # O que é o Django? (framework)
    pergunta3 = models.IntegerField(default=0)  # Em que ano foi criado o Django? (2005)
    pergunta4 = models.IntegerField(default=0)  # Em que ano foi criado o HTML? (1991)
    pergunta5 = models.CharField(max_length=50)  # O que significa CSS (cascading style sheet)

    def __str__(self):
        return f"{self.nome}"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    link_linkedin = models.URLField(max_length=200, blank=True)
    link_lusofona = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Projetos(models.Model):
    nome_do_projeto = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='media/', null=True)
    imagemGrande = models.ImageField(upload_to='media/', null=True)
    gif = models.ImageField(upload_to='media/', null=True)
    descricao = models.CharField(max_length=500)
    cadeira = models.CharField(max_length=100)
    ano_realizacao = models.IntegerField(default=0)
    participantes = models.ManyToManyField(Pessoa)
    link_github = models.URLField(max_length=200, blank=True)
    linguagens = models.CharField(max_length=100, blank=True)
    projetoDownload = models.FileField(blank=True)

    def __str__(self):
        return f"{self.nome_do_projeto}"


class Cadeira(models.Model):
    nome_cadeira = models.CharField(max_length=100)
    ano_realizado = models.IntegerField(default=0)
    ects = models.IntegerField(default=0)
    ranking = models.IntegerField(default=0)
    professores = models.ManyToManyField(Pessoa)
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE, related_name='portfolio.Cadeira.projeto+',
                                default=0)
    link_Lusofona = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome_cadeira}"


class Formacao(models.Model):
    sigla = models.CharField(max_length=10)
    nome_escola = models.CharField(max_length=100)
    link_escola = models.URLField(max_length=200, blank=True)
    curso = models.CharField(max_length=150)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.sigla}"


class Licenciatura(models.Model):
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    cadeiras = models.ManyToManyField(Cadeira)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.ano} {self.semestre}"


class Certificado(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='media/', null=True)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.nome}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to=resolution_path, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"


class Tecnologias(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=20)
    ano_criacao = models.IntegerField(default=0)
    criador = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='media/', null=True)
    link = models.URLField(max_length=200, blank=True)
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.nome}"


class TFC(models.Model):
    autores = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=0, related_name='portfolio.TFC.autores+')
    orientadores = models.ManyToManyField(Pessoa, related_name='portfolio.TFC.orientadores+')
    ano = models.IntegerField(default=0)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='media/', null=True)
    relatorio = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    video_demonstrativo = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.autores}"
