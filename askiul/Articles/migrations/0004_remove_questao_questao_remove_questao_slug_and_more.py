# Generated by Django 4.0.4 on 2022-05-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_alter_cadeira_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questao',
            name='questao',
        ),
        migrations.RemoveField(
            model_name='questao',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='slug',
        ),
        migrations.AlterField(
            model_name='resposta',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.questao'),
        ),
    ]