# Generated by Django 4.0.4 on 2022-05-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_post_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeira',
            name='projeto',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='projeto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio.Cadeira.projeto+', to='portfolio.projetos'),
        ),
        migrations.RemoveField(
            model_name='certificado',
            name='formacao',
        ),
        migrations.AddField(
            model_name='certificado',
            name='formacao',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='portfolio.formacao'),
        ),
        migrations.RemoveField(
            model_name='licenciatura',
            name='formacao',
        ),
        migrations.AddField(
            model_name='licenciatura',
            name='formacao',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='portfolio.formacao'),
        ),
    ]