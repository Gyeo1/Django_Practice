from django.contrib import admin
from .models import Profile

@admin.register(Profile)#여기 부분이 실제 웹 페이지에서 등록하는 부분이다.
class ProfileAdmin(admin.ModelAdmin):
    pass

# Register your models here.
