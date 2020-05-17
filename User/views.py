import datetime

import jwt
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import GenericViewSet

from App.models import User, Verifycode
from User.Defa import DefaultResponse
from User.SMS import send_sms
from User.message import USER_LOGIN_SUCCESS, USER_LOGIN_FAILED, INVALID_LOGIN_INFO
from User.userserializers import SmsSerializer, RegisterSerialize
from car_shopping.settings import SECRET_KEY


def index(request):

    return HttpResponse("ok")


@api_view(('POST', ))
def login(request):
    """登陆 (获取用户令牌)"""
    phone = request.data.get('phone')
    print(phone)

    if phone and len(phone)>=11:
        user = User.objects.filter(phone=phone).first()
        print(user)
        password1 =request.get('password')
        if password1 == user.password:

            # 用户登陆成功通过JWT生成用户身份令牌
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'data': {
                    'userid': user.id,
                }
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode()

            resp = DefaultResponse(*USER_LOGIN_SUCCESS, data={
                'token': token, 'phone': user.phone
            })
        else:
            resp = DefaultResponse(*USER_LOGIN_FAILED)
    else:
        resp = DefaultResponse(*INVALID_LOGIN_INFO)

    return resp



class SmsViewSET(CreateModelMixin,GenericViewSet):
    serializer_class = SmsSerializer
    print(serializer_class,'-----------')
    def create(self, request, *args, **kwargs):
        #获取手机号码
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        serializer.is_valid(raise_exception=True)
        # 发送信息
        print(phone,'222222222')
        #发送手机号码
        json = send_sms(phone)
        if json.get('code')==200:
    #保存到数据库表中
            # return Response({'msg': '发送成功', 'phone': phone}, status=200)
            vc = Verifycode.objects.create() .objects.create(phone=phone,code=json.get('obj'))
            if vc:
                return Response({'msg': '发送成功', 'phone': phone}, status=200)
        else:
            return Response({'msg':'验证码发送失败',}, status=400)

class RegisterSerializer(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class =  RegisterSerialize
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        # 密码加密
        password = serializer.validated_data['password']
        # password = make_password(password=password)
        serializer.validated_data['password'] = password
        #执行创建
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    def perform_create(self, serializer):
        serializer.save()






# class ChangePwd(View):
#     """
#     get : change_pwd  page
#     post: submit
#     """
#     def get(self, request):
#         pass

    # def post(self, request):
    #     json_str = request.body
    #     if not json_str:
    #         return Response('参数为空')
    #     dict_data = json.loads(json_str.decode('utf-8'))
    #     mobile = dict_data.get('mobile')
    #     old_password = dict_data.get('old_password')
    #     new_password = dict_data.get('new_password')
    #     sms_code = dict_data.get('sms_code')
    #     # 是否为空
    #     if not all([mobile, old_password, new_password, sms_code]):
    #         return HttpResponseForbidden('输入为空')
    #     # 手机格式
    #     if not re.match('^1[3-9]\d{9}$', mobile):
    #         return HttpResponseForbidden('手机号码格式输入错误')
    #     # 原密码格式错误
    #     if not re.match('^[0-9A-Za-z]{6,20}$', old_password):
    #         return HttpResponseForbidden('新密码格式不正确')
    #     # 新密码格式
    #     if not re.match('^[0-9A-Za-z]{6,20}$', new_password):
    #         return HttpResponseForbidden('新密码格式不正确')
    #     # 原密码和新密码
    #     if new_password == old_password:
    #         return HttpResponseForbidden('原密码和新密码相同，请重试')
    #     # 验证码格式是否正确
    #     if not sms_code.isnumeric():
    #         return ("请重新检查你的验证码是否正确    Forms ")
    #
    #     # 拿到当前对象user
    #     user = Users.objects.get(mobile=mobile)
    #     if user:
    #         if check_password(old_password, user.password):
    #             user.set_password(new_password)
    #             user.save()
    #             return to_json_data(errno=Code.OK, errmsg='恭喜你修改成功')
    #         else:
    #             return to_json_data(errno=Code.PARAMERR, errmsg='原密码错误')
    #     else:
    #         return to_json_data(errno=Code.PARAMERR, errmsg='不存在当前用户')
