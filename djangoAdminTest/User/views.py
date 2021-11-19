import json

from django.http import HttpResponse, JsonResponse

from django.contrib import auth

from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
# from ..User.common.register import Register
from User.common.register import Register


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
    print(data)
    username = data.get("username")
    password = data.get("password")
    # 调用django进行用户认证
    # 验证成功 user返回<class 'django.contrib.auth.models.User'>
    # 验证失败 user返回None
    user = auth.authenticate(username=username, password=password)
    print("user:", user)
    if user == None:
        result = False
        errorInfo = u"用户名或密码错误"
        return Response({"result": result, "detail": detail, "errorInfo": errorInfo})
    # 用户名和密码验证成功
    # 获取用户的token 如果没有token ，表示时用户首次登录，则进行创建，并且返回token
    try:
        tokenObj = Token.objects.get(user_id=user.id)
    except Exception as e:
        # token 不存在 说明是首次登录
        tokenObj = Token.objects.create(user=user)
    # 获取token字符串
    token = tokenObj.key
    return Response({"result": result, "detail": {'token': token}, "errorInfo": errorInfo})


@api_view(["POST"])
@permission_classes(())
@authentication_classes(())
def register(request):
    """注册"""
    data = request.data
    print("-----", data)
    res = Register().register(data)
    return Response(res)


@api_view(["GET"])
@permission_classes((AllowAny,))
@authentication_classes(())
def logout(request):
    """退出登录"""
    result = True
    errorInfo = u''
    token = ''
    authInfo = request.META.get('HTTP_AUTHORIZATION')
    print(authInfo)
    if authInfo:
        print(authInfo)
        token = authInfo.split(' ')[1]
    try:
        # 退出登录 删除token
        tokenObj = Token.objects.get(key=token)
        tokenObj.delete()
    except Exception as e:
        # traceback.print_exc(e)
        print('token not exist')
        result = False
        errorInfo = u'退出登录失败'
    return Response({"result": result, "detail": {}, "errorInfo": errorInfo})


@api_view(["GET"])
def getUserInfo(request):
    return Response({"result": "ok"})


@api_view(["GET"])
def testApi(request):
    return Response({"result": "ok"})
