# Generated by Django 4.1.5 on 2023-02-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV', '0002_show_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='cast',
            field=models.JSONField(default=[]),
        ),
    ]
