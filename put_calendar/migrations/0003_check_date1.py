# Generated by Django 2.1.4 on 2018-12-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put_calendar', '0002_check_date_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='check_date1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('work_title', models.CharField(max_length=34)),
            ],
        ),
    ]
