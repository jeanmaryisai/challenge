# Generated by Django 4.1 on 2022-12-20 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_cadeau_cadeau_quesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='fake_user',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fake_user',
            name='ip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
