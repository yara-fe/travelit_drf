# Generated by Django 4.2.3 on 2023-08-08 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0006_alter_reward_giver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reward',
            old_name='itinerary_id',
            new_name='itinerary',
        ),
    ]
