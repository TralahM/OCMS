# Generated by Django 2.1.3 on 2018-11-16 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20181116_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
