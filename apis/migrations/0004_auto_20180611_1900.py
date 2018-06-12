# Generated by Django 2.0.3 on 2018-06-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20180611_1653'),
    ]

    operations = [
         migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=70)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='apis.Tag'),
        ),
    ]
