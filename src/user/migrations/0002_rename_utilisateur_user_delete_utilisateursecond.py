# Generated by Django 5.1 on 2024-08-27 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='utilisateur',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='utilisateursecond',
        ),
    ]
