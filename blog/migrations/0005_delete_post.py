# Generated by Django 5.0.2 on 2024-03-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
