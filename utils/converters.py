# -*- coding: utf-8 -*-
# @Time : 2022/9/23 下午2:43
# @Author : WangYunfei
# @FileName: converters.py
# @Email: yunfei.wang@innvote.com
# 自定义路由转换器
# 验证当前用户名是否符合命名规则


class UsernameConverter:

    regex = "[a-zA-Z0-9_-]{5,20}"

    def to_python(self, value):
        return value

