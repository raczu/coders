# Generated by Django 3.0.2 on 2020-02-09 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='body',
            new_name='content',
        ),
    ]
