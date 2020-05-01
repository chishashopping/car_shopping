from rest_framework import serializers
from Home.models import Bootpage, Notice, Car


# 引导页
class BootpageSerializer(serializers.ModelSerializer):
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




