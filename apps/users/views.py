from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from users.models import User


class UsernameCountView(View):

    def get(self, request, username):
        # 1. 获取用户名称之后查询用户名称数量
        count = User.objects.filter(username=username).count()
        # 2. 返回响应
        return JsonResponse({"code": 0, "count": count, "errmsg": "ok"})






