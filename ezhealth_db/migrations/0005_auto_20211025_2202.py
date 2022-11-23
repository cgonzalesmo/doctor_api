# Generated by Django 3.1.7 on 2021-10-25 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezhealth_db', '0004_auto_20211025_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamber',
            name='friday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.fridaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='monday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.mondaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='saturday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.saturdaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='sunday_chamber',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.sundaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='thursday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.thursdaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='tuesday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.tuesdaychamber'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='wednesday_chamber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ezhealth_db.wednesdaychamber'),
        ),
    ]