# Generated by Django 3.1.7 on 2021-11-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezhealth_db', '0023_auto_20211126_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctorname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='appointment',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]