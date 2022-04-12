# Generated by Django 3.2.8 on 2022-04-12 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0002_auto_20220311_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiondetection',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario operador'),
        ),
    ]
