# Generated by Django 4.1.7 on 2023-03-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_shorturl_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.URLField(max_length=700, verbose_name=''),
        ),
    ]
