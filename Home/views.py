from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Home.homeserializers import BannerSerializer, NoticeSerializer
from Home.models import Bootpage, Notice


# 引导页
class BannerView(GenericAPIView):
    """
    GET:
    获取引导页图片信息
    """
    def get(self, request):
        # 数据查询
        img_queryset = Bootpage.objects.all()

        # 序列化
        img_data = BannerSerializer(img_queryset, many=True)
        return Response({
            'code':200,
            'msg':'请求成功',
            'data':{
                'img_info':img_data.data
            }
        })




# 公告
class NoticeView(GenericAPIView):
    """
    GET:
    获取公告信息
    """
    def get(self,request):
        # 数据查询
        notice_queryset = Notice.objects.all()

        # 序列化
        notice_data = NoticeSerializer(notice_queryset, many=True)
        return Response({
            'code':200,
            'message':'请求成功',
            'data':{
                'notice_info':notice_data.data

            }
        })


class SearchView(GenericAPIView):
    """
    POST:
    """
    def post(self,request):
        pass