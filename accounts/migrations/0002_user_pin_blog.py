# Generated by Django 2.0.3 on 2018-06-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20180611_1900'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pin_blog',
            field=models.ManyToManyField(to='apis.Blog'),
        ),
    ]
