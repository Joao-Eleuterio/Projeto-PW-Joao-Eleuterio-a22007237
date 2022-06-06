from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.urls import reverse

# Create your views here.
from .forms import PostForm, QuizzForm, ProjetosForm, NoticiaForm
from .models import Post, Quizz, Projetos, Licenciatura, Formacao, Certificado, Pessoa, Noticia, Tecnologias
from .quizzFunctions import desenha_grafico_resultados
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    context = {'licenciatura': Licenciatura.objects.all(), "data": [1, 2, 3, 4, 5]}
    return render(request, 'portfolio/licenciatura.html', context)


def projetos_page_view(request):
    context = {'projetos': Projetos.objects.all(), 'pessoa': Projetos.participantes}

    return render(request, 'portfolio/projetos.html', context)


def formacao_page_view(request):
    context = {'escolas': Formacao.objects.all()}
    return render(request, 'portfolio/formação.html', context)


def certificados_page_view(request):
    context = {'certificado': Certificado.objects.all()}
    return render(request, 'portfolio/certificados.html', context)


def quizz_page_view(request):
    form = QuizzForm(request.POST, use_required_attribute=False)
    desenha_grafico_resultados(Quizz.objects.all())
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {'form': form}

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
            return render(request, 'portfolio/sobreWebsite.html')
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Credenciais Invalidas"}
            )

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/login.html')
