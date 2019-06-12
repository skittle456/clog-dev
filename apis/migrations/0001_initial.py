# Generated by Django 2.0.3 on 2019-06-12 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('img_url', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=70, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('total_views', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('feedback_message', models.TextField()),
                ('email', models.EmailField(max_length=90)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(max_length=12, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('provider_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('provider_name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('favicon_url', models.URLField(blank=True, default=None, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=70)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insource',
            fields=[
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='apis.Blog')),
                ('total_likes', models.IntegerField(blank=True, default=0, null=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255)),
                ('blog_content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Provider'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='apis.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='insource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Insource'),
        ),
    ]
