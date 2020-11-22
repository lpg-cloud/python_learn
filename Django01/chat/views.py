from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request,'chat/index.html')


def room(request,room_name,user_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'userName': user_name,
    })

def login(request):
    """
    用户登录验证并存
    """

    print(dir(request))
    return HttpResponse('adfasdfasdf');
    if request.type=='get':
        print('方法是get')
       
    elif request.type=='post':
        print('方法是post')
        return HttpResponse('adfasdfasdf');