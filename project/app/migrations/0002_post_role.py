# Generated by Django 5.0.1 on 2024-01-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='role',
            field=models.CharField(default='user', max_length=255),
        ),
    ]
