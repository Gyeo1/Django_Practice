from . import views
from django.urls import path, re_path, register_converter


app_name='instagram' #URL Reverse에서 사용

class YearConverter:
    regex=r"20\d{2}"
    def to_python(self,value):
        return int(value)
    def to_url(self,value): #url_reverse할때 즉 어떤 값을 url 문자열로 리버싱할때 사용한다
        return "%04d"%value

register_converter(YearConverter, 'year') #YearConverter를 year이라 쓴다.

urlpatterns=[
    path('',views.post_list),
    #path(route, view,kwarg=None, name=None)의 구조로 1,2 파라매터는 필수이다
    #route는 url 경로 즉 사용된 경로, view는 함수 view나 class view를 지정해준다. 여기선 함수 view이다.
    #즉 웹 페이지가 기본 웹 페이지를 요청할 경우 views.post_list 함수를호출하도록 하는 내용이다.
    path('<int:pk>/',views.post_detail),

    #정규 표현식
    #path('archives/2020/',views.archives_year), #여기서 20xx도 해주고 싶다면? 아래처럼 정규 표현식을 사용!
    #path('archives/<int:year>/',views.archives_year), #이렇게 하면 year라는 인자값이 archives_year로 넘어간다.

    #여기서 int:year의 범위를 조정하고싶다면?
    #re_path(r'archives/(?P<year>20\d{2})/',views.archives_year),

    #CustomConverter를 사용할 경우path('archives/<컨버터 이름(여기서는 year):year>/',views.archives_year)
    path('archives/<year:year>/', views.archives_year),


]
