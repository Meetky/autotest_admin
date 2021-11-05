# -*- coding: utf-8 -*-
# @Project  :autotest_admin
# @File     :auth.py
# @Description: 
# @Date     :2021/11/5 16:28
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


# token过期处理
class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token, 大兄弟!")
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("大兄弟! User inactive or deleted.")

        # 过期验证
        if timezone.now() > (token.created + timedelta(seconds=10)):
            print("Token has expired!")
            raise exceptions.AuthenticationFailed("Token has expired!")
        return token.user, token
