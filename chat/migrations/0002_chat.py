# Generated by Django 2.1.3 on 2018-11-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=50)),
                ('group', models.CharField(default='', max_length=50)),
                ('body', models.CharField(max_length=50)),
            ],
        ),
    ]
