# Generated by Django 2.0.3 on 2018-07-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20180731_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insource',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255),
        ),
    ]
