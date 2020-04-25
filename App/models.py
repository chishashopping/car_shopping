# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BankCard(models.Model):
    card_name = models.CharField(max_length=30, blank=True, null=True)
    person_name = models.CharField(max_length=30, blank=True, null=True)
    card_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_card'


class Bootpage(models.Model):
    picture = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootpage'


class Car(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    car_style = models.CharField(max_length=100, blank=True, null=True)
    cartype_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shopping_points = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class CarCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_category'


class CarDetailed(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    country_id = models.IntegerField(blank=True, null=True)
    car_structure = models.CharField(max_length=30, blank=True, null=True)
    l_w_h = models.CharField(max_length=30, blank=True, null=True)
    car_volume = models.CharField(max_length=30, blank=True, null=True)
    drive_id = models.IntegerField(blank=True, null=True)
    car_engine = models.CharField(max_length=30, blank=True, null=True)
    car_change = models.CharField(max_length=30, blank=True, null=True)
    car_oil = models.CharField(max_length=30, blank=True, null=True)
    car_oilconsumption = models.CharField(max_length=30, blank=True, null=True)
    car_skylight = models.CharField(max_length=30, blank=True, null=True)
    car_lighting = models.CharField(max_length=30, blank=True, null=True)
    car_media = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_detailed'


class Country(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Dingdan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    carnum = models.IntegerField(blank=True, null=True)
    buynum = models.IntegerField()
    carcolor = models.CharField(max_length=4)
    buyway = models.CharField(max_length=4)
    money = models.IntegerField(blank=True, null=True)
    carcity = models.CharField(max_length=8, blank=True, null=True)
    signcity = models.CharField(max_length=8, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingdan'


class Drive(models.Model):
    drive_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drive'


class Fuwuzhongxing(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    state = models.IntegerField()
    where = models.CharField(max_length=50)
    who = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    phone = models.IntegerField()
    tjcailiao = models.CharField(max_length=255)
    tjmoney = models.IntegerField()
    shenke = models.IntegerField()
    ckshouyi = models.IntegerField(blank=True, null=True)
    tixian = models.IntegerField(blank=True, null=True)
    yongjinjilu = models.CharField(max_length=255, blank=True, null=True)
    tixianjilu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuwuzhongxing'


class Groupbuy(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_pattern = models.CharField(max_length=20, blank=True, null=True)
    g_firm = models.CharField(max_length=20, blank=True, null=True)
    g_brand = models.CharField(max_length=50, blank=True, null=True)
    g_style = models.CharField(max_length=50, blank=True, null=True)
    headcount = models.IntegerField(blank=True, null=True)
    headtruth = models.IntegerField(blank=True, null=True)
    r_time = models.DateTimeField(blank=True, null=True)
    g_img = models.CharField(max_length=30, blank=True, null=True)
    d_payment = models.FloatField(blank=True, null=True)
    integral = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groupbuy'


class Notice(models.Model):
    n_id = models.AutoField(primary_key=True)
    n_title = models.CharField(max_length=50)
    n_date = models.DateTimeField(blank=True, null=True)
    n_content = models.CharField(max_length=500, blank=True, null=True)
    n_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice'


class Opinion(models.Model):
    user_name = models.CharField(max_length=30, blank=True, null=True)
    opinion = models.CharField(max_length=255, blank=True, null=True)
    opinion_time = models.CharField(max_length=30, blank=True, null=True)
    opinion_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opinion'


class Parts(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_price = models.FloatField(blank=True, null=True)
    p_img = models.CharField(max_length=30, blank=True, null=True)
    b_name = models.CharField(max_length=50, blank=True, null=True)
    b_address = models.CharField(max_length=50, blank=True, null=True)
    p_details = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parts'


class Shangjiaruzhu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    state = models.IntegerField()
    where = models.CharField(max_length=50)
    who = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    phone = models.IntegerField()
    tjcailiao = models.CharField(max_length=255)
    tjmoney = models.IntegerField()
    shenke = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shangjiaruzhu'


class Store(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_img = models.CharField(max_length=50)
    s_address = models.CharField(max_length=100, blank=True, null=True)
    s_phone = models.CharField(max_length=11, blank=True, null=True)
    s_server = models.CharField(max_length=100, blank=True, null=True)
    s_price = models.CharField(max_length=100, blank=True, null=True)
    s_integrals = models.CharField(max_length=50, blank=True, null=True)
    s_detail = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class User(models.Model):
    name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=20)
    picture = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    is_deleted = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserSite(models.Model):
    user_site = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_site'


class Verify(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_phone = models.CharField(max_length=30, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verify'


class Wheel(models.Model):
    car_id = models.CharField(max_length=10, blank=True, null=True)
    car_name = models.CharField(max_length=30, blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wheel'
