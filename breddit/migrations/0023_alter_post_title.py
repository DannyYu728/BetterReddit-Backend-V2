# Generated by Django 4.1.3 on 2022-11-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breddit', '0022_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
