# Generated by Django 4.2.16 on 2024-10-13 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_rename_reservations_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='pnune_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='special_occasions',
            new_name='special_occasion',
        ),
    ]
