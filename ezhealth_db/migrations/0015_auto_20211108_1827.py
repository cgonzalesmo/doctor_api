# Generated by Django 3.1.7 on 2021-11-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezhealth_db', '0014_doctor_doctor_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]