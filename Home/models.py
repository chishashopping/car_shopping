# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json

from django.db import models


class Bank_Card(models.Model):
    id = models.IntegerField(primary_key=True)
    card_name = models.CharField(max_length=30, blank=True, null=True)
    person_name = models.CharField(max_length=30, blank=True, null=True)
    card_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_card'


class Bootpage(models.Model):
    bannerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    imgUrl = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootpage'


    def to_dict(self):
        return {
            'bannerid':self.bannerid,
            'name':self.name,
            'imgUrl':self.imgUrl
        }


class Car(models.Model):
    proid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    carType = models.CharField(max_length=100, blank=True, null=True)
    cartype_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    imgSmall = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=50, null=True),
    gbFlage = models.IntegerField(null=True)

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
    carStructure = models.CharField(max_length=30, blank=True, null=True)
    carLen = models.FloatField(blank=True, null=True)
    carWidth = models.FloatField(blank=True, null=True)
    carHeight = models.FloatField(blank=True, null=True)
    carEngine = models.CharField(max_length=30,blank=True, null=True)
    carTransmissionCase = models.CharField(max_length=30,blank=True, null=True)
    carFuel = models.CharField(max_length=30,blank=True, null=True)
    carOilConsumption = models.CharField(max_length=30,blank=True, null=True)
    carSkylight = models.CharField(max_length=30,blank=True, null=True)
    carLighting = models.CharField(max_length=30,blank=True, null=True)
    carMultiMedia = models.CharField(max_length=30,blank=True, null=True)
    carImg = models.CharField(max_length=500,blank=True,null=True)
    carTitle = models.CharField(max_length=30,blank=True,null=True)
    carWord = models.CharField(max_length=1000,blank=True,null=True)



    class Meta:
        managed = False
        db_table = 'car_detailed'

    def to_dict(self):
        obj = self.carImg
        obj_list = obj.split(';')
        d_list = []
        for i in obj_list:
            k_list = ['carImgid','carImgUrl']
            v_list = i.split(',')
            kv_dict = dict(zip(k_list,v_list))
            d_list.append(kv_dict)

        return {
            'carStructure':self.carStructure,
            'carLen':self.carLen,
            'carWidth':self.carWidth,
            'carHeight':self.carHeight,
            'carEngine':self.carEngine,
            'carTransmissionCase':self.carTransmissionCase,
            'carFuel':self.carFuel,
            'carOilConsumption':self.carOilConsumption,
            'carSkylight':self.carSkylight,
            'carLighting':self.carLighting,
            'carMultiMedia':self.carMultiMedia,
            'carImg':d_list,
            'carTitle':self.carTitle,
            'carWord':self.carWord

        }



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
    gbid = models.IntegerField(primary_key=True)
    gbbrand = models.CharField(max_length=20, null=True)
    gbcarType = models.CharField(max_length=20, null=True)
    gbimg = models.CharField(max_length=50, null=True)
    gbTotality = models.CharField(max_length=50, null=True)
    gbPerson = models.CharField(max_length=11, null=True)
    gbCountDown = models.CharField(max_length=11, null=True)
    gbStatus = models.IntegerField(blank=True, null=True)
    gbDate = models.CharField(max_length=20, null=True)
    gbIntgral = models.FloatField(blank=True, null=True)
    gbDownPayment = models.FloatField(blank=True, null=True)
    gborderid = models.IntegerField( blank=True, null=True)
    gbprice = models.FloatField(blank=True, null=True)
    gbcarColor = models.CharField(max_length=128, null=True)
    deposit = models.CharField(max_length=16, null=True)

    class Meta:
        managed = False
        db_table = 'groupbuy'

    # 团购商品信息数据
    def to_dict(self):
        return {
            'gbid':self.gbid,
            'gbbrand':self.gbbrand,
            'gbcarType':self.gbcarType,
            'gbimg':self.gbimg,
            'gbTotality':self.gbTotality,
            'gbPerson':self.gbPerson,
            'gbCountDown':self.gbCountDown,
            'gbDate' : self.gbDate,
            'gbIntgral' : self.gbIntgral,
            'gbDownPayment' : self.gbDownPayment,
            'gbStatus' : self.gbStatus,

        }

    # 团购确认订单数据
    def to_dict_gb_form(self):
        color = self.gbcarColor
        color_list = color.split('，')

        mortgage = Mortgage.objects.filter(gbid=self.gbid)
        mortgage_info = self.queryset_to_list(mortgage)
        return {
            'gborderid': self.gborderid,
            'img': self.gbimg,
            'gbbrand': self.gbbrand,
            'gbcarType': self.gbcarType,
            'gbprice': self.gbprice,
            'gbcarColor': color_list,
            'deposit': self.deposit,
            'mortgage': mortgage_info

        }

    def queryset_to_list(self, mortgage):
        res = []
        for obj in mortgage:
            res.append(obj.to_dict())
        return res


class Market(models.Model):
    afterid = models.IntegerField(auto_created=True, primary_key=True)
    address = models.CharField(max_length=128, null=True)
    afterimg = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=64, null=True)

    class Meta:
        managed = False
        db_table = 'market'

    def to_dict(self):
        return {
            'afterid':self.afterid,
            'address':self.address,
            'afterimg':self.afterimg,
            'name':self.name
        }


class Mortgage(models.Model):
    mortGageid = models.IntegerField(auto_created=True, primary_key=True)
    putDownOn = models.IntegerField(blank=True, null=True)
    monthly = models.IntegerField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    gbid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mortgage'

    def to_dict(self):
        return {
            'mortGageid': self.mortGageid,
            'putDownOn': self.putDownOn,
            'monthly': self.monthly,
            'stage': self.stage
        }


class Notice(models.Model):
    noticeid = models.AutoField(primary_key=True)
    noticeTitle = models.CharField(max_length=50)
    noticeTime = models.CharField(blank=True, null=True,max_length=50)
    noticeWord = models.CharField(max_length=600, blank=True, null=True)
    noticeImg = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice'

    def to_dict(self):
        return {
            'noticeid':self.noticeid,
            'noticeTitle':self.noticeTitle,
            'noticeTime':self.noticeTime,
            'noticeWord':self.noticeWord,
            'noticeImg':self.noticeImg
        }


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
    carShowid = models.IntegerField(auto_created=True, primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    minimg = models.CharField(max_length=128, blank=True, null=True)
    style = models.CharField(max_length=64, blank=True, null=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    displacement = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


    def to_dict(self):
        title = {
            'style': self.style,
            'brand': self.brand,
            'model': self.brand
        }


        return {
            "tilte": title,
            "carShowid": self.carShowid,
            "price": self.price,
            "stock": self.stock,
            "minimg": self.minimg,
            "style": self.style,
            "brand": self.brand,
            "model": self.model,
            "displacement": self.displacement
        }





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
