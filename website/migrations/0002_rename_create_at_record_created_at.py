# Generated by Django 4.2.1 on 2023-05-18 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
