# Generated by Django 4.1.3 on 2022-12-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breddit', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/static/oven.png', upload_to=''),
        ),
    ]
