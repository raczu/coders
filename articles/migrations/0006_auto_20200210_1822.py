# Generated by Django 3.0.2 on 2020-02-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200210_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='articlesPictures'),
        ),
    ]
