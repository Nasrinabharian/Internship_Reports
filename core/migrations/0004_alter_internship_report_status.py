# Generated by Django 3.2.6 on 2021-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_internship_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship_report',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Completed', 'Completed')], default='New', max_length=9),
        ),
    ]
