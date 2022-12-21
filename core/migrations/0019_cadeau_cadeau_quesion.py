# Generated by Django 4.1 on 2022-12-20 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_question_repliques_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadeau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
                ('cadeau', models.TextField()),
                ('show', models.BooleanField(default=False)),
                ('is_redeem', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='cadeau_quesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField()),
                ('reponse_true', models.TextField()),
                ('reponse_fake_1', models.TextField()),
                ('reponse_fake_2', models.TextField()),
                ('reponse_fake_3', models.TextField()),
                ('cadeau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadeau')),
            ],
        ),
    ]
