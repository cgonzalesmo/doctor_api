# Generated by Django 3.1.7 on 2021-11-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezhealth_db', '0021_auto_20211126_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='place',
            field=models.CharField(default='', max_length=20),
        ),
    ]
