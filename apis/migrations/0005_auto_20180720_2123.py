# Generated by Django 2.0.3 on 2018-07-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20180719_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
