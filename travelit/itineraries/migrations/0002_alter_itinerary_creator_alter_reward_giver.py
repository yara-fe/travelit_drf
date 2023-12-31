# Generated by Django 4.2.3 on 2023-08-08 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_itineraries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reward',
            name='giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to=settings.AUTH_USER_MODEL),
        ),
    ]
