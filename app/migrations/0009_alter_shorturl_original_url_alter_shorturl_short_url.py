# Generated by Django 4.1.7 on 2023-03-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_shorturl_original_url_alter_shorturl_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
