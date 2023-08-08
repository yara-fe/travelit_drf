# Generated by Django 4.2.3 on 2023-08-08 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraries', '0005_remove_reward_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to=settings.AUTH_USER_MODEL),
        ),
    ]