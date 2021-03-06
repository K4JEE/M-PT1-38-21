# Generated by Django 3.2.5 on 2021-08-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proekt', '0002_auto_20210819_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
