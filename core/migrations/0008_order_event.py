# Generated by Django 4.1 on 2023-09-01 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_question_is_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customevent'),
        ),
    ]
