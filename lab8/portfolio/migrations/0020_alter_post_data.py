# Generated by Django 4.0.4 on 2022-05-24 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 14, 15, 56, 155573)),
        ),
    ]
