# Generated by Django 2.2 on 2020-07-28 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confession', '0002_dislike_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]
