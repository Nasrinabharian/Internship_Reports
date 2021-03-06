# Generated by Django 3.2.6 on 2021-08-28 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_internship_report_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('receiver_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('file', models.FileField(default='', upload_to='media')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Completed', 'Completed')], default='New', max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='internship_report',
            name='file',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
