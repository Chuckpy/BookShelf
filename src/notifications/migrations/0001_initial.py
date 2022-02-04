# Generated by Django 3.1.8 on 2022-02-04 17:36

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
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('registration', models.DateTimeField(auto_now_add=True, null=True, verbose_name='data de cadastro')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='data de atualização')),
                ('status', models.CharField(blank=True, choices=[('read', 'Lido'), ('unread', 'Não Lido'), ('sended', 'Enviado'), ('unsended', 'Não Enviado !')], default='unread', max_length=264, null=True)),
                ('type_of_notification', models.CharField(blank=True, max_length=264, null=True)),
                ('user_receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_revoker', to=settings.AUTH_USER_MODEL)),
                ('user_sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
    ]