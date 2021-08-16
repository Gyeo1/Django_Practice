from django.contrib import admin
#아래부터 추가한 내용
from .models import Post,Comment
from django.utils.safestring import mark_safe
# Register your models here.

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag','message', 'message_length','update_at','is_public']
    list_display_links = ['message']
    search_fields = ['message']
    list_filter = ['create_at','is_public']
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
            #사진에 대한 접근이다{}안의 내용이 필수이며 .path나 .url 사용!
        return None
    def message_length(self,post):
        return len(post.message)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass