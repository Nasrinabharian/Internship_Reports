# Generated by Django 3.2.6 on 2021-08-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_internship_report_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship_report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='internship_report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
