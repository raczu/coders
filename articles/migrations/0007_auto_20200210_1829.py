# Generated by Django 3.0.2 on 2020-02-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200210_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='image',
        ),
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='articlesPictures'),
        ),
    ]
