# Generated by Django 3.1.8 on 2022-02-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_opensearch_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opensearch',
            name='own_product',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Produto em Busca'),
        ),
    ]
