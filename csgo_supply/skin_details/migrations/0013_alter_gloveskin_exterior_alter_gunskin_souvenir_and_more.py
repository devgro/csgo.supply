# Generated by Django 4.1.1 on 2022-10-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_details', '0012_alter_gunskin_gun_type_alter_gunskin_weapon_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gunskin',
            name='souvenir',
        ),
        migrations.RemoveField(
            model_name='gunskin',
            name='stattrak',
        ),
        migrations.RemoveField(
            model_name='knifeskin',
            name='stattrak',
        ),
    ]
