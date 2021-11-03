import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.contrib import auth

from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# Create your views here.


def index(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        if req["username"] == "admin" and req["password"] == "admin":
            return JsonResponse({"code": 200, "message": "success"})
        else:
            return
    else:
        return HttpResponse("Hello World")


@api_view(["POST"])
@permission_classes((AllowAny,))
@authentication_classes(())
def login(request):
    """登录"""
    result = True
    errorInfo = u""
    detail = {}
    data = request.data
    username = data.get("username")
    password = data.get("password")

    user = auth.authenticate(username=username, password=password)
    print("user: ", user)
