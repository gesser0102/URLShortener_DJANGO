# Generated by Django 4.1.7 on 2023-03-16 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_shorturl_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.URLField(max_length=700, validators=[django.core.validators.RegexValidator(message='Invalid URL', regex='^https?://(?:www\\.|(?!www))[^\\s\\.]+\\.[^\\s]{2,}$')], verbose_name=''),
        ),
    ]