# Generated by Django 3.1.8 on 2022-01-21 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220120_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dislike',
            options={'verbose_name': 'Não Curtidos', 'verbose_name_plural': 'Não Curtidos'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Curtidos', 'verbose_name_plural': 'Curtidos'},
        ),
        migrations.AlterModelOptions(
            name='opensearch',
            options={'verbose_name': 'Aberto para Busca', 'verbose_name_plural': 'Abertos para Busca'},
        ),
    ]
