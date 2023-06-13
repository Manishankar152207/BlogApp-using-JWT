from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
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
