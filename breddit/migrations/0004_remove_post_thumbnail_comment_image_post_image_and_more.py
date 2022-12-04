# Generated by Django 4.1.3 on 2022-12-04 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breddit', '0003_alter_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='user',
            name='banner',
            field=models.ImageField(blank=True, upload_to='banners'),
        ),
    ]