# Generated by Django 3.0.7 on 2020-06-07 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='questio',
            new_name='question',
        ),
    ]
