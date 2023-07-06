from django.contrib import admin
from .models import Post
from .models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'content', 'created_at', 'view_count', 'writer']     # 내용을 직접 볼 수 있도록
    # list_editable = ['content', 'writer']         # 내용, 작성자를 바로 수정할 수 있도록
    list_filter = ['created_at']        # 날짜 순으로 필터를 걸어 정렬
    search_fields = ['id', 'writer__username']      # id, 글 작성자 검색 가능하도록
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다'      # 검색 기능 사용에 대한 도움말
    readonly_fields = ['view_count', 'created_at']
    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content = '운영 규칙 위반으로 인한 게시글 삭제 처리'
            item.save()