# Generated by Django 2.2.5 on 2019-09-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('matricula', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
