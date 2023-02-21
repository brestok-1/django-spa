from django.contrib import admin

from blog.models import Tags, Article, Comment


# Register your models here.
class TagsAdmin(admin.TabularInline):
    model = Tags
    extra = 1


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = (TagsAdmin,)
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class ArticlesAdmin(admin.ModelAdmin):
    pass
