# Generated by Django 3.0.8 on 2020-08-07 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0005_presence_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presence',
            old_name='email',
            new_name='student',
        ),
    ]
