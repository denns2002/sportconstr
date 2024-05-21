from django.contrib import admin

from cms.models import CMS


@admin.register(CMS)
class CMSAdmin(admin.ModelAdmin):
    list_display = ['slug', 'content_type']
    list_filter = ['content_type']
    search_fields = [
        'id', 'slug', 'content_type', 'char', 'text',
        'image', 'integer', 'float', 'datetime', 'bool'
    ]
    readonly_fields = ['slug', 'id']
    fields = search_fields

