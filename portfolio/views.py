import urllib

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.urls import reverse

# Create your views here.
from django.utils.baseconv import base64

from .forms import PostForm, QuizzForm, NoticiaForm, TFCForm, ProjetosForm, CadeiraForm, LicenciaturaForm
from .models import Post, Quizz, Projetos, Licenciatura, Formacao, Certificado, Noticia, Tecnologias, TFC, Cadeira
from .quizzFunctions import cria_grafico
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    context = {'licenciatura': Licenciatura.objects.all(), "data": [1, 2, 3, 4, 5]}
    return render(request, 'portfolio/licenciatura.html', context)


@login_required
def nova_Cadeira_view(request):
    if request.method == 'POST':
        form = CadeiraForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    form = CadeiraForm()
    context = {'form': form}
    return render(request, 'portfolio/novaCadeira.html', context)


@login_required
def edita_Licenciatura_view(request, licenciatura_id):
    licenciatura = Licenciatura.objects.get(id=licenciatura_id)
    form = LicenciaturaForm(request.POST or None, instance=licenciatura)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'licenciatura_id': licenciatura_id}
    return render(request, 'portfolio/editaLicenciatura.html', context)


@login_required
def edita_Cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editaCadeira.html', context)


def projetos_page_view(request):
    form = TFCForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))
    context = {'projetos': Projetos.objects.all(), 'pessoa': Projetos.participantes, 'TFC': TFC.objects.all(),
               'formTFC': form}

    return render(request, 'portfolio/projetos.html', context)


@login_required
def novo_Projeto_view(request):
    if request.method == 'POST':
        form = ProjetosForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))

    form = ProjetosForm()
    context = {'form': form}
    return render(request, 'portfolio/novoProjeto.html', context)


@login_required
def edita_Projeto_view(request, projeto_id):
    projeto = Projetos.objects.get(id=projeto_id)
    form = ProjetosForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editaProjeto.html', context)


def formacao_page_view(request):
    context = {'escolas': Formacao.objects.all()}
    return render(request, 'portfolio/formação.html', context)


def certificados_page_view(request):
    context = {'certificado': Certificado.objects.all()}
    return render(request, 'portfolio/certificados.html', context)


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    context = {'form': form, 'data': cria_grafico(Quizz.objects.all())}
    if form.is_valid():
        form.save()
        return render(request, 'portfolio/quizz.html', context)

    return render(request, 'portfolio/quizz.html', context)


def blog_page_view(request):
    context = {'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def nova_Post_view(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/novablog.html', context)


def edita_Post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/editablog.html', context)


@login_required
def apaga_Post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def sobreWebsite_page_view(request):
    context = {'tecnologias': Tecnologias.objects.all()}
    return render(request, 'portfolio/sobreWebsite.html', context)


def noticia_page_view(request):
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'portfolio/noticia.html', context)


@login_required
def nova_Noticia_view(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:noticia'))

    form = NoticiaForm()
    context = {'form': form}
    return render(request, 'portfolio/novaNoticia.html', context)


@login_required
def edita_Noticia_view(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    form = NoticiaForm(request.POST or None, instance=noticia)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:noticia'))

    context = {'form': form, 'noticia_id': noticia_id}
    return render(request, 'portfolio/editaNoticia.html', context)


@login_required
def apaga_Noticia_view(request, noticia_id):
    Noticia.objects.get(id=noticia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:noticia'))


def login_page_view(request):
    if request.method == "POST":
        nome_login = request.POST.get('username')
        password_login = request.POST.get('password')
        utilizador = authenticate(request, username=nome_login, password=password_login)

        if utilizador is not None:
            login(request, utilizador)
            return render(request, 'portfolio/home.html')
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Credenciais Invalidas"}
            )

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/login.html')
