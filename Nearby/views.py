from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework.response import Response

from Nearby.Myfilters import MarketFilter
from Nearby.models import Hotcity, Market, Prolist, Market_Prolist
from Nearby.nearby_serializers import HotcitySerializer, MarketSerializer, ShophomeSerializer


class City(APIView):
    def get(self,request):
        queryset = Hotcity.objects.all()
        hotcity_serializer = HotcitySerializer(queryset,many=True)
        return Response({
            'code': 200,
            'msg': "请求成功",
            'hotcity': hotcity_serializer.data
        })

class Nearby_market(ListAPIView):
    """
    附近的服务商家显示
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_class = MarketFilter


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'code': '200',
            'message': '请求成功',
            'data': serializer.data
        })



class ShopHome(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_class = MarketFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset[0].afterid)
        mp = Market_Prolist.objects.filter(afterid=queryset[0].afterid).all()
        print(mp)
        mp_list = [i.proid for i in mp]
        print(mp_list)
        queryset2 = Prolist.objects.filter(proid__in=mp_list)
        shophome_serializer = ShophomeSerializer(queryset2, many=True)
        print(queryset2)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'code': '200',
            'message': '请求成功',
            'data': serializer.data,
            'prolist': shophome_serializer.data
        })