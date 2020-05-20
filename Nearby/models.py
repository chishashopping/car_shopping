from django.db import models

# Create your models here.
class Hotcity(models.Model):
    id = models.IntegerField(primary_key=True)
    cityname = models.CharField(max_length=50, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'hotcity'


class Market(models.Model):
    afterid = models.IntegerField(auto_created=True, primary_key=True)
    address = models.CharField(max_length=128, null=True)
    afterimg = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=64, null=True)

    class Meta:
        managed = False
        db_table = 'market'


class Prolist(models.Model):
    proid = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=128, null=True)
    price = models.FloatField(blank=True, null=True)
    introduction = models.CharField(max_length=256, null=True)
    presentexp =models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'prolist'


class Market_Prolist(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    afterid = models.IntegerField(blank=False, null=False)
    proid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'market_prolist'
