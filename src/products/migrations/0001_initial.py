# Generated by Django 3.1.8 on 2022-02-01 16:43

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields
import products.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OpenSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
            ],
            options={
                'verbose_name': 'Aberto para Busca',
                'verbose_name_plural': 'Abertos para Busca',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to=products.models.upload_product, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Imagem do Produto',
                'verbose_name_plural': 'Imagens do Produto',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=130, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, help_text='Fale brevemente sobre o produto e suas caracteristicas mais importantes', max_length=1000, verbose_name='Descrição')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Descrição Curta')),
                ('product_information', models.TextField(blank=True, help_text='Descreva como esta o estado do produto', max_length=1000, verbose_name='Informação do Produto')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='Quantidade em estoque')),
                ('available', models.BooleanField(default=True, verbose_name='Disponível')),
                ('search_bool', models.BooleanField(default=True, help_text='Caso o booleano estiver ativo esse produto pode entrar na lista de troca de outros, o padrão é ativo', verbose_name='Procurando')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': "Tag's",
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Categoria-Raiz')),
            ],
            options={
                'verbose_name': 'Sub-Categoria',
                'verbose_name_plural': 'Sub-Categorias',
                'ordering': ('name',),
            },
        ),
    ]
