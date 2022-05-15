# Generated by Django 4.0.4 on 2022-05-15 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('descricao', models.CharField(max_length=300)),
                ('image', models.ImageField(default='\\images\\default.png', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('descricao', models.CharField(max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('cadeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.cadeira')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('resposta', models.CharField(max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.questao')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
