# Generated by Django 4.0.5 on 2022-06-19 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reports',
            old_name='volume',
            new_name='Volume',
        ),
    ]