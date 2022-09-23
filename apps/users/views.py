# -*- coding: utf-8 -*-
import json
import re

from django.contrib.auth import login
from django.http import JsonResponse
# from django.shortcuts import render

# Create your views here.
from django.views import View

from users.models import User


class UsernameCountView(View):

    def get(self, request, username):
        """
        获取用户名的数量
        :param request:
        :param username:
        :return:
        """
        # 1. 获取用户名称之后查询用户名称数量
        count = User.objects.filter(username=username).count()
        # 2. 返回响应
        return JsonResponse({"code": 0, "count": count, "errmsg": "ok"})


class RegisterView(View):

    def post(self, request):
        body_bytes = request.body
        body_str = body_bytes.decode()
        body_dict = json.loads(body_str)

        username = body_dict.get("username")
        password = body_dict.get("password")
        password2 = body_dict.get("password2")
        mobile = body_dict.get("mobile")
        allow = body_dict.get("allow")

        # 数据校验
        if not all([username, password, password2, mobile]):
            return JsonResponse({"code": 400, "errmsg": "参数不全!"})
        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return JsonResponse({"code": 400, "errmsg": "用户名格式错误!"})
        # 判断密码是否是8-20个数字
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return JsonResponse({"code": 400, "errmsg": "密码格式有误!"})
        # 判断两次密码是否一致
        if password != password2:
            return JsonResponse({"code": 400, "errmsg": "两次密码不一致!"})
        # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return JsonResponse({"code": 400, "errmsg": "手机号格式有误!"})
        # 判断是否勾选用户协议
        if not isinstance(allow, bool) or not allow:
            return JsonResponse({"code": 400, "errmsg": "请确认协议!"})

        # 数据入库
        user = User.objects.create_user(username=username, password=password, mobile=mobile)

        # 状态保持
        login(request, user)

        return JsonResponse({"code": 0, "errmsg": "ok"})


