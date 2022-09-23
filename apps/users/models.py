from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# class User(models.Model):
#
#     # 用户名是否可以重复 unique=True  True:不能重复
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11, unique=True)


# 使用系统自带的用户模型类
# AbstractUser

class User(AbstractUser):

    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "tb_users"
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


"""
如果使用的时Django内置的用户模型类
    需要在settings中使用用户模型类的指定
    
    自定义的模型类会与内置模型类冲突
"""




