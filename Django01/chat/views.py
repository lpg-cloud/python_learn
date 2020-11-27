from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from chat.models import client


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name, user_name):
    onlineUsers = client.objects.all()

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'userName': user_name,
        'onlineUsers': onlineUsers
    })


def login(request):
    """
    用户登录验证并存
    """

    print(dir(request))
    return HttpResponse('adfasdfasdf');
    if request.type == 'get':
        print('方法是get')

    elif request.type == 'post':
        print('方法是post')
        return HttpResponse('adfasdfasdf');
