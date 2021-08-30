from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from . import form
urlpatterns=[
    path('login/', LoginView.as_view(
        form_class=form.LoginForm,
        template_name='accounts/login_form.html'), name='login'),
    path('profile/',views.profile, name='profile'), #이렇게 하면 profile url로 이동시 views의 profile로 가 랜더링 된다.
    path('profile/edit',views.profile_edit, name='profile_edit'),
    path('signup/',views.signup, name='signup'),
    path('logout/',LogoutView.as_view(), name='logout'),
]