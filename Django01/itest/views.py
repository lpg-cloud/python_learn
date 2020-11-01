from django.shortcuts import render
from django.conf import Settings

# Create your views here.
from django.shortcuts import HttpResponse

user_list = []
for i in range(1, 15):
    user_list.append({'name': 'name'+str(i), 'age': i, 'sex': "男"})


def index(request):
    if request.method == 'POST':
        temUser = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'sex': request.POST.get('sex'),
        }
        user_list.append(temUser)
    return render(request, 'index.html', {'userList': user_list})


def detail(request, *args, **kwargs):
    print(args)
    print(kwargs)
    a = HttpResponse('asdfasdf')
    print(a)
    return a
