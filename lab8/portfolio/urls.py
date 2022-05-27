from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('certificados', views.certificados_page_view, name='certificados'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('blog', views.blog_page_view, name='blog'),
    path('nova/', views.nova_Post_view, name='nova'),
    path('edita/<int:post_id>', views.edita_Post_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_Post_view, name='apaga'),
    path('sobreOWebsite', views.sobreOWebsite_page_view, name='sobreOWebsite'),
    path('noticia', views.noticia_page_view, name='noticia'),
]
