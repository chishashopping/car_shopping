# Generated by Django 2.2 on 2020-05-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Card',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('card_name', models.CharField(blank=True, max_length=30, null=True)),
                ('person_name', models.CharField(blank=True, max_length=30, null=True)),
                ('card_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bank_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bootpage',
            fields=[
                ('bannerid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('imgUrl', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'bootpage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('proid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('carType', models.CharField(blank=True, max_length=100, null=True)),
                ('cartype_id', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('imgSmall', models.CharField(blank=True, max_length=200, null=True)),
                ('gbFlage', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'car_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarDetailed',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('country_id', models.IntegerField(blank=True, null=True)),
                ('carStructure', models.CharField(blank=True, max_length=30, null=True)),
                ('carLen', models.FloatField(blank=True, null=True)),
                ('carWidth', models.FloatField(blank=True, null=True)),
                ('carHeight', models.FloatField(blank=True, null=True)),
                ('carEngine', models.CharField(blank=True, max_length=30, null=True)),
                ('carTransmissionCase', models.CharField(blank=True, max_length=30, null=True)),
                ('carFuel', models.CharField(blank=True, max_length=30, null=True)),
                ('carOilConsumption', models.CharField(blank=True, max_length=30, null=True)),
                ('carSkylight', models.CharField(blank=True, max_length=30, null=True)),
                ('carLighting', models.CharField(blank=True, max_length=30, null=True)),
                ('carMultiMedia', models.CharField(blank=True, max_length=30, null=True)),
                ('carImg', models.CharField(blank=True, max_length=500, null=True)),
                ('carTitle', models.CharField(blank=True, max_length=30, null=True)),
                ('carWord', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'car_detailed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dingdan',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('carnum', models.IntegerField(blank=True, null=True)),
                ('buynum', models.IntegerField()),
                ('carcolor', models.CharField(max_length=4)),
                ('buyway', models.CharField(max_length=4)),
                ('money', models.IntegerField(blank=True, null=True)),
                ('carcity', models.CharField(blank=True, max_length=8, null=True)),
                ('signcity', models.CharField(blank=True, max_length=8, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('img', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dingdan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'drive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fuwuzhongxing',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('state', models.IntegerField()),
                ('where', models.CharField(max_length=50)),
                ('who', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('tjcailiao', models.CharField(max_length=255)),
                ('tjmoney', models.IntegerField()),
                ('shenke', models.IntegerField()),
                ('ckshouyi', models.IntegerField(blank=True, null=True)),
                ('tixian', models.IntegerField(blank=True, null=True)),
                ('yongjinjilu', models.CharField(blank=True, max_length=255, null=True)),
                ('tixianjilu', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fuwuzhongxing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupbuy',
            fields=[
                ('gbid', models.IntegerField(primary_key=True, serialize=False)),
                ('gbbrand', models.CharField(max_length=20, null=True)),
                ('gbcarType', models.CharField(max_length=20, null=True)),
                ('gbimg', models.CharField(max_length=50, null=True)),
                ('gbTotality', models.CharField(max_length=50, null=True)),
                ('gbPerson', models.CharField(max_length=11, null=True)),
                ('gbCountDown', models.CharField(max_length=11, null=True)),
                ('gbStatus', models.IntegerField(blank=True, null=True)),
                ('gbDate', models.CharField(max_length=20, null=True)),
                ('gbIntgral', models.FloatField(blank=True, null=True)),
                ('gbDownPayment', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groupbuy',
                'managed': False,
            },
        ),
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
            name='Notice',
            fields=[
                ('noticeid', models.AutoField(primary_key=True, serialize=False)),
                ('noticeTitle', models.CharField(max_length=50)),
                ('noticeTime', models.CharField(blank=True, max_length=50, null=True)),
                ('noticeWord', models.CharField(blank=True, max_length=600, null=True)),
                ('noticeImg', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('opinion', models.CharField(blank=True, max_length=255, null=True)),
                ('opinion_time', models.CharField(blank=True, max_length=30, null=True)),
                ('opinion_type', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'opinion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_price', models.FloatField(blank=True, null=True)),
                ('p_img', models.CharField(blank=True, max_length=30, null=True)),
                ('b_name', models.CharField(blank=True, max_length=50, null=True)),
                ('b_address', models.CharField(blank=True, max_length=50, null=True)),
                ('p_details', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'parts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shangjiaruzhu',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('state', models.IntegerField()),
                ('where', models.CharField(max_length=50)),
                ('who', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('tjcailiao', models.CharField(max_length=255)),
                ('tjmoney', models.IntegerField()),
                ('shenke', models.IntegerField()),
            ],
            options={
                'db_table': 'shangjiaruzhu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('carShowid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('minimg', models.CharField(blank=True, max_length=128, null=True)),
                ('style', models.CharField(blank=True, max_length=64, null=True)),
                ('brand', models.CharField(blank=True, max_length=64, null=True)),
                ('model', models.CharField(blank=True, max_length=64, null=True)),
                ('displacement', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('picture', models.CharField(blank=True, max_length=150, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('is_deleted', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_site', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('user_email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'verify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(blank=True, max_length=10, null=True)),
                ('car_name', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'wheel',
                'managed': False,
            },
        ),
    ]