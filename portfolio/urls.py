from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('aa', views.aa_page_view, name='aa'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('certificados', views.certificados_page_view, name='certificados'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('blog', views.blog_page_view, name='blog'),
    path('novablog/', views.nova_Post_view, name='novablog'),
    path('editablog/<int:post_id>', views.edita_Post_view, name='editablog'),
    path('apagablog/<int:post_id>', views.apaga_Post_view, name='apagablog'),
    path('sobreWebsite', views.sobreWebsite_page_view, name='sobreWebsite'),
    path('noticia', views.noticia_page_view, name='noticia'),
    path('novaNoticia/', views.nova_Noticia_view, name='novaNoticia'),
    path('editaNoticia/<int:noticia_id>', views.edita_Noticia_view, name='editaNoticia'),
    path('apagaNoticia/<int:noticia_id>', views.apaga_Noticia_view, name='apagaNoticia'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
]
