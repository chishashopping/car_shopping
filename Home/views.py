from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Home.homeserializers import BannerSerializer, NoticeSerializer, GroupBuySerializer
from Home.models import Bootpage, Notice, Groupbuy, CarDetailed
import json


# 引导页
from Home.paging import LimitSet


class BannerView(GenericAPIView):
    """
    GET:
    获取引导页图片信息
    """
    def queryset_to_list(self,img_querset):
        res = []
        for obj in img_querset:
            res.append(obj.to_dict())
        return res


    def get(self, request,*args,**kwargs):
        img_queryset = Bootpage.objects.all()
        img_info = self.queryset_to_list(img_queryset)
        return Response({
            'code':200,
            'msg':'请求成功',
            'data': img_info
        })




# 公告
class NoticeView(GenericAPIView):
    """
    GET:
    获取公告信息
    """
    def queryset_to_list(self,querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res

    def get(self,request):
        # 数据查询
        notice_queryset = Notice.objects.all()
        notice_info = self.queryset_to_list(notice_queryset)
        return Response({
            'code':200,
            'message':'请求成功',
            'data': notice_info
        })


# 搜索
class SearchView(GenericAPIView):
    """
    POST:
    搜索页面
    """
    def post(self,request):
        pass



# 团购
class GroupBuyView(GenericAPIView):
    """
    GET:
    团购列表
    """
    queryset = Groupbuy.objects.all()
    serializer_class = GroupBuySerializer
    pagination_class = LimitSet

    def queryset_to_list(self,querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res

    def get(self, request, *args, **kwargs):
        r_data = request.GET
        count = r_data.get('count')
        gb_queryset = Groupbuy.objects.filter(gbStatus=count)
        gb_info = self.queryset_to_list(gb_queryset)
        return Response({
            'code': 200,
            'message': '请求成功',
            'data':gb_info
        })


class GbProduct(GenericAPIView):
    """
    GET:
    团购商品信息
    """
    def queryset_to_list(self,querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res

    def get(self,request,*args,**kwargs):
        r_data = request.GET
        gbid = r_data.get('gbid')
        product_querset = Groupbuy.objects.filter(gbid=gbid)




        product_info = self.queryset_to_list(product_querset)

        return Response({
            'code': 200,
            'message': '请求成功',
            'data': product_info
        })


class GbDetailView(GenericAPIView):
    """
    GET:
    根据访问的商品id获取该商品的详细资料
    """

    def queryset_to_list(self, querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res

    def get(self, request, *args, **kwargs):
        r_data = request.GET
        gbid = r_data.get('gbid')
        car_querset = CarDetailed.objects.filter(id=gbid)

        car_info = self.queryset_to_list(car_querset)

        return Response({
            'code': 200,
            'message': '请求成功',
            'data': car_info
        })

