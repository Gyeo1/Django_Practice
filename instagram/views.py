from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from .models import Post  # 모델 파일에서 Post 함수 가져오기
from .forms import PostForm

@login_required
def post_new(request):
    if request.method=='POST': #만약 POST 메소드 발생시
        form=PostForm(request.POST, request.FILES) #POST와 파일을 인자값으로
        if form.is_valid(): # 인자로 받은 값에 대해서 유효성을 검증 , 검증 성공한 값을 사전형으로 제공받음 제대로 제공 받으면 FORM의 역할끝!
            post = form.save(commit=False)  # 필요에 따라 DB에 저장하기 #commit을 False로 두면 post.save가 아직 안옴
            post.author = request.user  # 현재 로그인 유저 인스턴스를 받아옴
            post.save()  # 받고 나서 post.save 실행 // 주의사항! 로그인을 보장 받아야 된다. 따라서 @ 위에다 붙이기

            messages.success(request, '포스팅을 저장했습니다.')  # messages 등록!
            return redirect(post)
        else:
            form.errors #검증실패시 오류정보 저장.
    else:#GET 요청일때
        form=PostForm()
    return render(request,'instagram/post_form.html',
                  {
                      'form':form,
                      'post':None, #새로 만들때는 post값을 none으로 준다
                  })
@login_required
def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)

    #작성자 check Tip!
    if post.author != request.user: #만약 사용자가 다르면 딴곳으로 보내라.
        messages.error(request,'작성자만 수정 할 수 있습니다!')
        return redirect(post)

    if request.method=='POST': #만약 POST 메소드 발생시
        form=PostForm(request.POST, request.FILES, instance=post) #POST와 파일을 인자값으로
        if form.is_valid(): # 인자로 받은 값에 대해서 유효성을 검증 , 검증 성공한 값을 사전형으로 제공받음 제대로 제공 받으면 FORM의 역할끝!
            post=form.save()    #필요에 따라 DB에 저장하기 #commit을 False로 두면 post.save가 아직 안옴

            messages.success(request, '포스팅을 수정했습니다.')  # messages 등록!
            return redirect(post)
        else:
            form.errors #검증실패시 오류정보 저장.
    else:#GET 요청일때
        form=PostForm(instance=post)
    return render(request,'instagram/post_form.html',
                  {
                      'form':form,
                      'post':post, #수정할 시에는 post값을 그대로 반환!
                  })

# @login_required   #로그인 데코레이션
# def post_list(request):#호출 당시의 모든 내역을 전달 받는 함수!
#     qs=Post.objects.all() #Post의 모든 객체를 쿼리해서 가져온다
#     q=request.GET.get('q','') #''은  키가 없을 때 빈칸을 반환 한다는 의미이다.
#     if q: #q라는 검색어가 있다면 여서긴 빈칸도 가능하기 때문에 모든 내용을 가져옴
#         qs=qs.filter(message__icontains=q) #qs즉 모든 객체에서 q라는 내용을 필터링해서 다시 넣는다.
#
#     messages.info(request,'messages Test입니다') #messages 등록!
#
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q,
#     })
# post_list=ListView.as_view(model=Post,paginate_by=10) #이 한줄이 위의 내용을 포함한다. 근데 응용이 어렵다!

# @method_decorator(login_required,name='dispatch')
class PostList(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 10

post_list=PostList.as_view()

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

# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")
post_archive=ArchiveIndexView.as_view(model=Post, date_field='create_at') #ArchiveIndexView 실습내용! 최신목록 보여주기
post_archive_year=YearArchiveView.as_view(model=Post, date_field='create_at', make_object_list=True)