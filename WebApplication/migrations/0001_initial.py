# Generated by Django 3.2.5 on 2021-07-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.IntegerField()),
                ('Month', models.CharField(max_length=30)),
                ('Bp_Values', models.IntegerField()),
                ('User_name', models.CharField(max_length=30)),
                ('Hospital', models.CharField(max_length=30)),
            ],
        ),
    ]