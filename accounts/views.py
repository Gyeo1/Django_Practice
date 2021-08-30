from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, UpdateView, CreateView
from accounts.form import ProfileForm
from accounts.models import Profile

@login_required
def profile(request):
    return render(request,'accounts/profile.html')

#아래는 위의 내용을 CBV로 만들 경우!
# class ProfileView(LoginRequiredMixin,TemplateView):
#     template_view='accounts/profile.html'
# profile=ProfileView.as_view()

@login_required
def profile_edit(request):
    try:
        profile= request.user.profile #요청을한 유저의 프로필을 가져온다
    except Profile.DoesNotExist:
        profile=None
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('profile') #여기서 profile은 위의 profile 함수의 url로 보내는것.
    else:
        form=ProfileForm(instance=profile)
    return render(request,'accounts/profile_form.html',{
        'form':form,
    })

# class ProfileUpdateView(LoginRequiredMixin,UpdateView):
#     model = Profile
#     form_class = ProfileForm
# profile_edit = ProfileUpdateView.as_view()

User=get_user_model() #절대models에서 받아오지 마라!
signup=CreateView.as_view(
    model=User,
    form_class=UserCreationForm,
    success_url=settings.LOGIN_URL,
    template_name='accounts/signup_form.html'
)

def logout(request):
    pass