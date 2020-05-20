'''
# -*- coding:utf-8 -*-
# @Time:2020/5/18 22:45
# @Author:chisha
# @Description:
'''
import django_filters
from django_filters import rest_framework as filters

from Nearby.models import Market

class MarketFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    shopid = django_filters.NumberFilter(field_name='afterid')
    class Meta:
        model = Market
        fields = {
            'name',
            'shopid',
        }
