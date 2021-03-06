# Generated by Django 4.0.4 on 2022-06-08 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_noticia_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TFC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0)),
                ('titulo', models.CharField(max_length=50)),
                ('resumo', models.CharField(max_length=500)),
                ('imagem', models.ImageField(null=True, upload_to='media/')),
                ('relatorio', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('video_demonstrativo', models.URLField(blank=True)),
                ('autores', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio.TFC.autores+', to='portfolio.pessoa')),
                ('orientadores', models.ManyToManyField(related_name='portfolio.TFC.orientadores+', to='portfolio.pessoa')),
            ],
        ),
    ]
