import re

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            'message', 'photo', 'is_public', 'tag_set'
        ]

    def clean_message(self):
        message=self.cleaned_data.get('message')
        if message:
            message=re.sub(r'[a-zA-Z]+','',message)# 패턴의 값을 바꾸겠다는 식 (바꾸고 싶은 값의 범위, 바꿀값, 적용 대상) 즉 영어지우기다.
        return message