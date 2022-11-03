from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from accounts.models import Member
from .KeywordFind import *
from django.views.decorators.csrf import csrf_exempt
from .models import Sentence
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
    return render(request, 'record/index.html', {
        'is_logined': bool(login_id),
        'login_id': login_id,
        'nickname': nickname
    })
# @csrf_exempt


def sentence(request):
    response_data = {
        # 설계한 대로 응답 데이터를 정리해주면 된다.
        'status': 200,
        'msg': 'success',
        'data': []  # dictionary 형태로 서빙을 해주면 여러개를 서빙하기 곤란하다.
    }

    if request.method == 'GET':
        keyword_decode = parse.unquote(parse.unquote(keyword))
        response_data['data'] = KeywordFind(keyword_decode)
        #
        # from .KeywordFind.py import KeywordFind(keyword)
        # 는 keyword가 들어있는 문장들을 list로 반환한다.
        #

        return JsonResponse(response_data)
        # return HttpResponse('sentence function ready')
    elif request.method == 'POST':
        # response_data['data'] = KeywordFind(request.POST["keyword_2"])
        sentence_queryset = Sentence.objects.filter(
            content__contains=request.POST["keyword_2"]).order_by('-like_count')
        # ORDERING을 좋아요를 많이 받은 순서로 정렬한다.
        for query in sentence_queryset:
            response_data['data'].append(
                [
                    query.id,
                    query.content.strip(),
                    query.like_count,
                    query.unlike_count
                ]
            )
            #
            # from .KeywordFind.py import KeywordFind(keyword)
            # 는 keyword가 들어있는 문장들을 list로 반환한다.
            #

        return JsonResponse(response_data)


def update(request):
    for sentence in HRsentences_set:
        DBsentences_queryset = Sentence.objects.all()
        DBsentences = []
        for query in DBsentences_queryset:
            DBsentences.append(query.content)

        if sentence in DBsentences:
            pass
        else:
            Sentence.objects.create(content=sentence)
    return HttpResponse('update complete!')


def like(request, sentence_id):
    login_id = request.session.get('login_id', False)
    # id에 접근해서, login_id를 가진 Member의 like_posts에 접근
    # print(login_id)

    response_data = {
        # 설계한 대로 응답 데이터를 정리해주면 된다.
        'status': 200,
        'msg': 'success',
        'data': None  # dictionary 형태로 서빙을 해주면 여러개를 서빙하기 곤란하다.
    }

    liked_sentence = Sentence.objects.get(id=int(sentence_id))
    liked_sentence.like_count += 1
    liked_sentence.save()

    liked_member = Member.objects.get(login_id=login_id)
    liked_member.like_posts.add(liked_sentence)

    response_data['data'] = liked_sentence.like_count
    # member =
    return JsonResponse(response_data)


def unlike(request, sentence_id):
    login_id = request.session.get('login_id', False)
    # id에 접근해서, login_id를 가진 Member의 like_posts에 접근
    # print(login_id)

    response_data = {
        # 설계한 대로 응답 데이터를 정리해주면 된다.
        'status': 200,
        'msg': 'success',
        'data': None  # dictionary 형태로 서빙을 해주면 여러개를 서빙하기 곤란하다.
    }

    unliked_sentence = Sentence.objects.get(id=int(sentence_id))
    unliked_sentence.unlike_count += 1
    unliked_sentence.save()

    unliked_member = Member.objects.get(login_id=login_id)
    unliked_member.unlike_posts.add(unliked_sentence)

    response_data['data'] = unliked_sentence.unlike_count
    # member =
    return JsonResponse(response_data)
