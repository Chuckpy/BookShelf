# Generated by Django 3.1.8 on 2022-01-20 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('name', models.CharField(blank=True, help_text='Coloque o nome do seu projeto ou empresa.', max_length=50, verbose_name='Nome do Projeto')),
                ('short_name', models.CharField(blank=True, help_text='Coloque uma sigla de até 3 caracteres.', max_length=3, verbose_name='Nome Curto')),
                ('subtitle', models.CharField(blank=True, help_text='Subtítulo ou descrição utilizada no site.', max_length=50, verbose_name='Subtítulo')),
                ('favicon', models.ImageField(blank=True, help_text='Ícone pequeno utilizado na aba dos navegadores (Resolução 32x32 px em formato .png)', null=True, upload_to='uploads/config/img/', verbose_name='Ícone')),
                ('default_rank', models.ForeignKey(blank=True, help_text='O cliente recebe esse ranking no cadastro (Importante existir)', null=True, on_delete=django.db.models.deletion.CASCADE, to='ranking.rank', verbose_name='Ranking Inicial')),
            ],
            options={
                'verbose_name': 'Configuração',
                'verbose_name_plural': 'Configurações',
            },
        ),
    ]
