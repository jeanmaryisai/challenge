# Generated by Django 4.1 on 2022-12-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_question_repliques_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='repliques',
            field=models.ManyToManyField(blank=True, related_name='persone_avoir_repondu', to='core.concurent'),
        ),
        migrations.AlterField(
            model_name='question',
            name='repliques_rate',
            field=models.ManyToManyField(blank=True, to='core.concurent'),
        ),
    ]
