from django.contrib import admin

from blog.models import Post, Tag, Comment


class TagAdmin(admin.ModelAdmin):
    raw_id_fields = ("posts",)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ("post", "author")


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("likes", "tags", )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)




