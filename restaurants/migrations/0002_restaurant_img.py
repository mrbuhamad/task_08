# Generated by Django 2.1.5 on 2020-01-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
