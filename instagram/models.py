from django.db import models

# Create your models here.
class Post(models.Model):
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    is_public=models.BooleanField(default=False, verbose_name='공개 여부')
    photo=models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')#upload_to는 해당 이름의 폴더에 저장한다는 뜻이다.
                                                                            #%y,m,d는 년 월일의 개념
    def __str__(self):
        #return f"Custom Post Object({self.id})"
        return self.message
#     def message_length(self):
#         return len(self.message)
# #auto_now와 auto_now_add는 자동으로 시각이 입력되는 개념이다
