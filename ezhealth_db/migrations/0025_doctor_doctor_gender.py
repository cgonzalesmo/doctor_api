# Generated by Django 3.1.7 on 2021-12-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezhealth_db', '0024_auto_20211129_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
