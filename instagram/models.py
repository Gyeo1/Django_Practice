from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message=models.TextField(
        validators=[MinLengthValidator(10)]#최소 10글자는 써라
    )
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    is_public=models.BooleanField(default=False, verbose_name='공개 여부')
    photo=models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')#upload_to는 해당 이름의 폴더에 저장한다는 뜻이다.
                                                                            #%y,m,d는 년 월일의 개념
    tag_set=models.ManyToManyField('Tag')
    def __str__(self):
        #return f"Custom Post Object({self.id})"
        return self.message
    def get_absolute_url(self):
        return reverse('instagram:post_detail',args=[self.pk])
    class Meta:#meta class로 정렬하기 설정
        ordering=['-id'] #역순임 지금


class Comment(models.Model): #Comment 외래키의 예시
    post=models.ForeignKey(Post, on_delete=models.CASCADE,
                           limit_choices_to={'is_public':True}) #실제 db에서는 psot_id 필드가 생성이더ㅚㄴ다.
    #Post 모델을 대상으로 한다. Post 대신 'Post'도 가능함. 다른앱.class명도 가능
    message=models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name= models.CharField(max_length=50, unique=True)
    #포스트와 태그 관계를 M2M을하자. 어느 클래스에다 해도 무관함
  #  post_set=models.ManyToManyField(Post,blank=True)
    def __str__(self):
        return self.name

#     def message_length(self):
#         return len(self.message)
# #auto_now와 auto_now_add는 자동으로 시각이 입력되는 개념이다
