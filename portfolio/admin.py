from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Post, Cadeira, Licenciatura, Formacao, Quizz, Projetos, Pessoa, Certificado, Noticia, Tecnologias, \
    TFC


class participantes(admin.ModelAdmin):
    filter_horizontal = ('participantes',)


class professores(admin.ModelAdmin):
    filter_horizontal = ('professores',)


class licenciatura(admin.ModelAdmin):
    filter_horizontal = ('cadeiras',)


class TFC_autor_orientadores(admin.ModelAdmin):
    filter_horizontal = ('orientadores',)


admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Projetos, participantes)
admin.site.register(Pessoa)
admin.site.register(Cadeira, professores)
admin.site.register(Licenciatura, licenciatura)
admin.site.register(Formacao)
admin.site.register(Certificado)
admin.site.register(Noticia)
admin.site.register(Tecnologias)
admin.site.register(TFC, TFC_autor_orientadores)
