# Generated by Django 5.1.3 on 2024-11-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_post', '0001_initial'),
        ('api_user', '0002_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='api_post.post'),
        ),
    ]
