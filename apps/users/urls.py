# -*- coding: utf-8 -*-
# @Time : 2022/9/23 下午2:35
# @Author : WangYunfei
# @FileName: urls.py
# @Email: yunfei.wang@innvote.com
from django.urls import path
from . import views

urlpatterns = [
    path('usernames/<username>/count/', views.UsernameCountView.as_view()),
]


