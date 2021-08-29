from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


@login_required
def profile(request):
    return render(request,'accounts/profile.html')

#아래는 위의 내용을 CBV로 만들 경우!
# class ProfileView(LoginRequiredMixin,TemplateView):
#     template_view='accounts/profile.html'
# profile=ProfileView.as_view()

def profile_edit(request):
    render(request,'accounts/profile_edit.html')