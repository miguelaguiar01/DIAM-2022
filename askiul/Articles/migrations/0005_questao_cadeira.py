# Generated by Django 4.0.4 on 2022-05-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_remove_questao_questao_remove_questao_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='Cadeira',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Articles.cadeira'),
            preserve_default=False,
        ),
    ]
