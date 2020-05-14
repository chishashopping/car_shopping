from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Home.MyPaginatons import StoreListPager
from Home.homeserializers import BannerSerializer, NoticeSerializer, GroupBuySerializer, StoreSerializer, \
    MarketSerializer
from Home.models import Bootpage, Notice, Groupbuy, CarDetailed, Store, Market
import json

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
    团购基本配置
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


class HomeCarshopView(GenericAPIView):
    """
    车商城列表接口
    GET:
    根据提交的页数和数据量，返回相关数据
    """

    def queryset_to_list(self, querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res
    queryset = Store.objects.all()
    pagination_class = StoreListPager
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        r_data = request.GET
        limit = r_data.get('limit')
        count = r_data.get('count')
        StoreListPager.page_size = limit
        StoreListPager.page = count
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            store_info = self.queryset_to_list(page)
            return Response({
                "code": 200,
                "message": "请求成功",
                "data": store_info
            })

        store_info = self.queryset_to_list(queryset)
        return Response({
                "code": 200,
                "message": "请求成功",
                "data": store_info
            })


class MarketView(GenericAPIView):
    """
    后市场
    GET
    根据提交的页数和数据量，返回相关数据
    """

    def queryset_to_list(self, querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res

    queryset = Market.objects.all()
    pagination_class = StoreListPager
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        r_data = request.GET
        limit = r_data.get('limit')
        count = r_data.get('count')
        StoreListPager.page_size = limit
        StoreListPager.page = count
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            market_info = self.queryset_to_list(page)
            return Response({
                "code": 200,
                "message": "请求成功",
                "data": market_info
            })

        market_info = self.queryset_to_list(queryset)
        return Response({
            "code": 200,
            "message": "请求成功",
            "data": market_info
        })