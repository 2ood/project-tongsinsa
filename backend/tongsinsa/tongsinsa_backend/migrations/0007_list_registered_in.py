# Generated by Django 3.2.16 on 2022-12-29 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tongsinsa_backend', '0006_auto_20221229_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='registered_in',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
