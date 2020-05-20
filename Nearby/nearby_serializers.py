'''
# -*- coding:utf-8 -*-
# @Time:2020/5/18 0:28
# @Author:chisha
# @Description:
'''
from rest_framework import serializers

from Nearby.models import Hotcity, Market, Prolist


class HotcitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotcity
        fields = "__all__"


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"


class ShophomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prolist
        fields = "__all__"