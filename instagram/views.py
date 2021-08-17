from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post  # 모델 파일에서 Post 함수 가져오기

post_list=ListView.as_view(model=Post) #이 한줄이 아래 모든 내용을 포함한다. 근데 응용이 어렵다!

# def post_list(request):#호출 당시의 모든 내역을 전달 받는 함수!
#     qs=Post.objects.all() #Post의 모든 객체를 쿼리해서 가져온다
#     q=request.GET.get('q','') #''은  키가 없을 때 빈칸을 반환 한다는 의미이다.
#     if q: #q라는 검색어가 있다면 여서긴 빈칸도 가능하기 때문에 모든 내용을 가져옴
#         qs=qs.filter(message__icontains=q) #qs즉 모든 객체에서 q라는 내용을 필터링해서 다시 넣는다.
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#     })
#render로 html응답을 받아온다. 장고의 template 시스템을 활용하기 위한 함수.
#render함수의 가운데 경로는 실제 instagram 내부의 경로로 실제 경로를 만들어 줘야 된다.
#여기서 template의 post_list는 {}안의 post_list를 참조한다.

def post_detail(request:HttpRequest, pk:int)->HttpResponse: #타입 힌트의 개념 #pk 가 capture된 문자열이다
    response=HttpResponse()
    response.write("Hello world!")
    return response



