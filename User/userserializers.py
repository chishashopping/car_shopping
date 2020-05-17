import code
import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# 发短信的
from App.models import User


class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11, error_messages={'max_length': '必须输入11位验证码',
                                                                                'min_length': '必须输入11位验证码', })

    def validate_phone(self, phone):
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('此手机号码已注册，请登录')
        if not re.match(r'1[35789]\d{9}', phone):
            raise serializers.ValidationError('手机号码格式错误')
        return phone


class RegisterSerialize(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4, error_messages={
        'required': '必须输入手机验证码',
        'max_length': '必须输入4位验证码',
        'min_length': '必须输入4位验证码',
    }, write_only=True)

    # name = serializers.CharField(required=True, allow_blank=False,
    #                                  validators=[UniqueValidator(queryset=User.objects.all(), message='此用户名已被占用')])
    repassword = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [ 'password', 'repassword', 'phone', 'code']

    #验证code是否正确，并且是否过期
    # def validate_code(self, code):
    #     print('----->inital:', self.initial_data)
    #     verifycodes = Verifycode.objects.filter(phone=self.initial_data['phone'])
    #     print('----->validate_code:', verifycodes)
        #.order_by('-update_time')
        # if verifycodes:
        #     verifycode = verifycodes.first()
        #     if verifycode.code == code:
        #         return code
            # 设置一个过期时间
            # time_delta = datetime.now() - timedelta(minutes=10)
            # if time_delta > verifycode.update_time:
            #     raise serializers.ValidationError('验证码过期，请重新发送')
            # if verifycode.code != code:
            #     raise serializers.ValidationError('验证码错误')
        # else:
        #     raise serializers.ValidationError('请发送验证码')
        # return code
    def validated_code(self):
        if code !=None:
            return code

    def validate(self, attrs):
        if attrs['password'] != attrs['repassword']:
            raise serializers.ValidationError('两次密码不一致')
        del attrs['repassword']
        del attrs['code']
        return attrs

    # def validate_username(self, username):
    #     if User.objects.filter(username=username).exists():
    #         raise serializers.ValidationError('此手机号码已注册，请登录')
    #     return username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'phone','id']




