from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),

    # LICENCIATURA
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('novaCadeira', views.nova_Cadeira_view, name='novaCadeira'),
    path('editaLicenciatura/<int:licenciatura_id>', views.edita_Licenciatura_view, name='editaLicenciatura'),
    path('editaCadeira/<int:cadeira_id>', views.edita_Cadeira_view, name='editaCadeira'),
    path('apagaLicenciatura/<int:cadeira_id>', views.licenciatura_page_view, name='apagaLicenciatura'),

    # PROJETOS
    path('projetos', views.projetos_page_view, name='projetos'),
    path('editaProjeto/<int:projeto_id>', views.edita_Projeto_view, name='editaProjeto'),
    path('apagaprojetos/<int:projeto_id>', views.projetos_page_view, name='apagaprojetos'),
    path('novoProjeto', views.novo_Projeto_view, name='novoProjeto'),

    # FORMACAO
    path('formacao', views.formacao_page_view, name='formacao'),
    path('editaformacao/<int:projetos_id>', views.formacao_page_view, name='editaformacao'),
    path('apagaformacao/<int:projetos_id>', views.formacao_page_view, name='apagaformacao'),
    path('novaformacao', views.formacao_page_view, name='novaformacao'),

    # CERTIFICADOS
    path('certificados', views.certificados_page_view, name='certificados'),
    path('editacertificados/<int:certificados_id>', views.certificados_page_view, name='editacertificados'),
    path('apagacertificados/<int:certificados_id>', views.certificados_page_view, name='apagacertificados'),
    path('novacertificados', views.certificados_page_view, name='novacertificados'),

    # BLOG
    path('blog', views.blog_page_view, name='blog'),
    path('novablog/', views.nova_Post_view, name='novablog'),
    path('editablog/<int:post_id>', views.edita_Post_view, name='editablog'),
    path('apagablog/<int:post_id>', views.apaga_Post_view, name='apagablog'),

    # NOTICIA
    path('noticia', views.noticia_page_view, name='noticia'),
    path('novaNoticia/', views.nova_Noticia_view, name='novaNoticia'),
    path('editaNoticia/<int:noticia_id>', views.edita_Noticia_view, name='editaNoticia'),
    path('apagaNoticia/<int:noticia_id>', views.apaga_Noticia_view, name='apagaNoticia'),

    # COMPETENCIAS | QUIZZ | SOBREWEBSITE
    path('competencias', views.competencias_page_view, name='competencias'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('sobreWebsite', views.sobreWebsite_page_view, name='sobreWebsite'),

    # LOGIN | LOGOUT
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
]

#TODO
# video

