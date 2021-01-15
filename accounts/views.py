from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Member
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    elif request.method == 'POST':
        print(request.POST)
        login_id = request.POST["login_id"]
        login_pw = request.POST["login_pw"]

        #check id
        member = Member.objects.filter(login_id=login_id).first()
        if member: # 만약 입력한 login_id와 일치하는 id의 Member 가 있다면,
            if login_pw == member.login_pw:
                request.session['login_id'] = login_id
                # request.session은 dictionary 형태를 띄고 있고, 그 안에
                # 새로운 key로서 'login_id'를 만들어 value로 login_id를 넣어준다.
                # session을 사용하지않으면, session_id 를 발급하지 않는다.
                # session_id 를 임시로 다 발급하는 사이트도 있는 것이고,
                # 회원만 session_id를 발급하는 사이트도 있는 것이다. 개발자 마음이다.

                # return HttpResponse('Hello HaengBaal')
                return HttpResponseRedirect(reverse('record:index'))
            else:
                return render(request, 'accounts/login.html', {
                    'login_error': '아이디 또는 패스워드가 일치하지 않습니다.'
                }) # 실패했을 때만, dictionary를 전달한다.
        else:
            return render(request, 'accounts/login.html', {
                'login_error': '아이디 또는 패스워드가 일치하지 않습니다.'
            }) # 실패했을 때만, dictionary를 전달한다.

def logout(request):
    try:
        del request.session['login_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('record:index'))
