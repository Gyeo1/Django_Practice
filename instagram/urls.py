from . import views
from django.urls import path
urlpatterns=[
    path('',views.post_list),
    #path(route, view,kwarg=None, name=None)의 구조로 1,2 파라매터는 필수이다
    #route는 url 경로 즉 사용된 경로, view는 함수 view나 class view를 지정해준다. 여기선 함수 view이다.
    #즉 웹 페이지가 기본 웹 페이지를 요청할 경우 views.post_list 함수를호출하도록 하는 내용이다.
    path('<int:pk>/',views.post_detail),
]