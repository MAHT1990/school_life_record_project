from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from accounts.models import Member
from .KeywordFind import KeywordFind
from django.views.decorators.csrf import csrf_exempt
# 같은 폴더내에 KeywordFind.py 에서 KeywordFind 함수를 가져온다.
import json
from urllib import parse
# Create your views here.

# @csrf_exempt
def index(request):
    login_id = request.session.get('login_id', False)
    member = Member.objects.filter(login_id=login_id).first()
    if member:
        nickname = member.nickname
        # 두 번째 인자는 False 기본값이다.
        # request의 sessions의 login_id를 읽어와서, login_id에 할당하는데,
        # 로그인을 하면 session에 'login_id' 값을 부여받게 되고,
        # 로그인을 하지않으면, session자체가 없어서 False 값(default값)을 login_id에 할당한다.
    else:
        nickname = None
    return render(request,'record/index.html',{
        'is_logined': bool(login_id),
        'login_id': login_id,
        'nickname': nickname
    })
# @csrf_exempt
def sentence(request, keyword):
    response_data = {
    # 설계한 대로 응답 데이터를 정리해주면 된다.
    'status': 200,
    'msg': 'success',
    'data': None # dictionary 형태로 서빙을 해주면 여러개를 서빙하기 곤란하다.
    }

    if request.method == 'GET':
        keyword_decode = parse.unquote(parse.unquote(keyword))
        # TODO: Encoding 문제 해결. 한글을 받아라!
        response_data['data'] = KeywordFind(keyword_decode)
            #
            #from .KeywordFind.py import KeywordFind(keyword)
            #는 keyword가 들어있는 문장들을 list로 반환한다.
            #

        return JsonResponse(response_data)
        # return HttpResponse('sentence function ready')
    elif request.method == 'POST':
        response_data['data'] = KeywordFind(request.POST["keyword_2"])
            #
            #from .KeywordFind.py import KeywordFind(keyword)
            #는 keyword가 들어있는 문장들을 list로 반환한다.
            #

        return JsonResponse(response_data)
        # return JsonResponse({'status': 2020})
        # return HttpResponse('sentence function ready')

def update(request):
    return HttpResponse('update goes here!')
