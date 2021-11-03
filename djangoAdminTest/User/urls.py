# -*- coding: utf-8 -*-
# @Project  :django_admin_test
# @File     :urls.py.py
# @Description: 
# @Date     :2021/10/29 14:07
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login")
]
