# Generated by Django 3.1.8 on 2022-01-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
        ('core_config', '0002_auto_20220115_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='configapp',
            name='default_rank',
            field=models.ForeignKey(blank=True, help_text='O cliente recebe esse ranking no cadastro (Importante existir)', null=True, on_delete=django.db.models.deletion.CASCADE, to='ranking.rank', verbose_name='Ranking Inicial'),
        ),
    ]
