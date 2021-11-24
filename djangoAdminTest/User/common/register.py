# -*- coding: utf-8 -*-
# @Project  :autotest_admin
# @File     :register.py
# @Description: 
# @Date     :2021/11/16 17:00
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
from django.contrib.auth.models import User
import pymysql


class Register:
    def __init__(self):
        self.response = {"result": True, "detail": {}, "errorInfo": ""}

    def query_username(self):
        """查询表中所有用户"""
        db = pymysql.connect(user="root", password="123456", host="127.0.0.1",
                             port=3306, database="autotest_admin")
        cursor = db.cursor()
        sql = "select username from auth_user"
        cursor.execute(sql)
        all_users = cursor.fetchall()
        return all_users

    def register(self, data):
        username = data.get("username")
        password = data.get("password1")
        email = data.get("email")
        print("用户提交的注册信息：", username, password, email)
        if username in [user[0] for user in self.query_username()]:
            # 判断用户是否存在，存在
            self.response["errorInfo"] = "用户名已存在"
        else:
            # 用户不存在则新建
            user = User.objects.create_user(username, email, password)
            self.response["detail"]["msg"] = "注册成功"
            print("user:--", user)
        return self.response
