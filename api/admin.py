from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    # list_display = (
    #     "id",
    #     "name"
    # )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    # list_display = (
    #     "id",
    #     "name"
    # )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "created_at",
        "published",
    )
    list_filter = (
        "title",
        "created_at",
        "published"
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            # "subtitle",
        )
    }
