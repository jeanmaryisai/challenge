# Generated by Django 4.1 on 2022-12-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_concurent_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_unique',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='question',
            name='repliques',
        ),
        migrations.AddField(
            model_name='question',
            name='repliques',
            field=models.BooleanField(default=True),
        ),
    ]
