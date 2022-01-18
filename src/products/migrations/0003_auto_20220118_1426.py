# Generated by Django 3.1.8 on 2022-01-18 14:26

from django.db import migrations
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220116_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='created',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='updated',
        ),
        migrations.AddField(
            model_name='products',
            name='uuid',
            field=model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
