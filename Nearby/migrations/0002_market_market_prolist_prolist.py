# Generated by Django 2.2 on 2020-05-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nearby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('afterid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=128, null=True)),
                ('afterimg', models.CharField(max_length=128, null=True)),
                ('name', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'market',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Market_Prolist',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('afterid', models.IntegerField()),
                ('proid', models.IntegerField()),
            ],
            options={
                'db_table': 'market_prolist',
            },
        ),
        migrations.CreateModel(
            name='Prolist',
            fields=[
                ('proid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('introduction', models.CharField(max_length=256, null=True)),
                ('presentexp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prolist',
            },
        ),
    ]
