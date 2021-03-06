from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ("posts",)


# @admin.register(Post) is an alternative to the admin.site.register below
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
