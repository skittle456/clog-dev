# Generated by Django 2.0.3 on 2018-07-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_provider_description'),
        ('accounts', '0002_user_pin_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow_provider',
            field=models.ManyToManyField(to='apis.Provider'),
        ),
    ]
