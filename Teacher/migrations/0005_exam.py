# Generated by Django 3.2.5 on 2021-07-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0004_auto_20210717_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=50)),
                ('date', models.TextField(max_length=50)),
                ('time_start', models.TextField(max_length=5)),
                ('time_end', models.TextField(max_length=5)),
            ],
        ),
    ]
