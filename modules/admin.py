from django.contrib import admin

from .models.news import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
