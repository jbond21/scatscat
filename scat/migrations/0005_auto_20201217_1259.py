# Generated by Django 3.0.7 on 2020-12-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0004_auto_20201216_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='questions',
            new_name='set',
        ),
    ]