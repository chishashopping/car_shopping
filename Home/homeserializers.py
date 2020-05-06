from rest_framework import serializers
from Home.models import Bootpage, Notice, Car, Groupbuy


# 引导页
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootpage
        fields = "__all__"


# 公告
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"

# 搜索
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

# 团购列表
class GroupBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupbuy
        fields = "__all__"




