# Generated by Django 3.2.6 on 2021-08-28 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210828_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload2',
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
        migrations.RenameField(
            model_name='upload',
            old_name='file',
            new_name='upload',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='description',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='receiver_name',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='status',
        ),
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]