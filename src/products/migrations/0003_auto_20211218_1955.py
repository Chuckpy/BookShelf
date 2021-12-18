# Generated by Django 3.1.8 on 2021-12-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211210_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'ordering': ['position'], 'verbose_name': 'Imagem do Produto', 'verbose_name_plural': 'Imagens do Produto'},
        ),
        migrations.AddField(
            model_name='productimages',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Posição'),
        ),
    ]
