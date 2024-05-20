from django.contrib import admin

from cms.models import CMS


@admin.register(CMS)
class CMSAdmin(admin.ModelAdmin):
    list_display = ['slug', 'content_type']
    list_filter = ['content_type']
    search_fields = [
        'slug', 'content_type', 'char', 'text',
        'image', 'integer', 'float', 'datetime'
    ]
    readonly_fields = ['slug']


