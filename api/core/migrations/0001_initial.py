# Generated by Django 3.1.2 on 2020-10-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
            ],
        ),
    ]
