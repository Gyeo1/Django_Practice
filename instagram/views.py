from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView ,DetailView
from .models import Post  # 모델 파일에서 Post 함수 가져오기



# def post_list(request):#호출 당시의 모든 내역을 전달 받는 함수!
#     qs=Post.objects.all() #Post의 모든 객체를 쿼리해서 가져온다
#     q=request.GET.get('q','') #''은  키가 없을 때 빈칸을 반환 한다는 의미이다.
#     if q: #q라는 검색어가 있다면 여서긴 빈칸도 가능하기 때문에 모든 내용을 가져옴
#         qs=qs.filter(message__icontains=q) #qs즉 모든 객체에서 q라는 내용을 필터링해서 다시 넣는다.
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#     })
post_list=ListView.as_view(model=Post,paginate_by=10) #이 한줄이 위의 내용을 포함한다. 근데 응용이 어렵다!

#render로 html응답을 받아온다. 장고의 template 시스템을 활용하기 위한 함수.
#render함수의 가운데 경로는 실제 instagram 내부의 경로로 실제 경로를 만들어 줘야 된다.
#여기서 template의 post_list는 {}안의 post_list를 참조한다.

# def post_detail(request:HttpRequest, pk:int)->HttpResponse: #타입 힌트의 개념 #pk 가 capture된 문자열이다
#     # try:
#     #     post=Post.objects.get(pk=pk)#뒤의 pk는 함수 인자 pk와 같다.
#     # except Post.DoesNotExist:
#     #     raise Http404
#
#     post=get_object_or_404(Post,pk=pk) #위의 내용을 한줄로 간단하게!
#
#     return render(request,'instagram/post_detail.html',{
#         'post':post,
#     })
class PostDetailView(DetailView): #DetailView를 상속받는 클래스 생성
    model = Post
    #queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs=super().get_queryset() #부모의 쿼리셋을 받아온다는 뜻이다.
        if not self.request.user.is_authenticated:
            qs=qs.filter(is_public=True)
        return qs

# post_detail=DetailView.as_view(model=Post,
#                                queryset=Post  .objects.filter(is_public=True),
#                                )  #CBV로 할 경우
post_detail=PostDetailView.as_view()

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
