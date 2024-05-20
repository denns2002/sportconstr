from django.contrib import admin

from projects.models.project_models import *
from projects.models.style_models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['style', 'sample']
    search_fields = [
        'user', 'slug', 'name', 'created_at',
        'sample', 'style', 'modules'
    ]
    readonly_fields = ['slug', 'created_at']
    filter_horizontal = ['modules']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['req_modules']
    search_fields = ['name', 'req_modules']
    filter_horizontal = ['req_modules']
    readonly_fields = ['slug']


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['modules']
    search_fields = ['name', 'description', 'tags']
    filter_horizontal = ['modules']
    readonly_fields = ['slug']


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ['slug', 'typography', 'palette']
    list_filter = ['typography', 'palette']
    search_fields = list_filter
    readonly_fields = ['slug']


@admin.register(Typography)
class TypographyAdmin(admin.ModelAdmin):
    list_display = ['name', 'font']
    list_filter = ['font']
    search_fields = list_display
    readonly_fields = ['slug']


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_color', 'secondary_color', 'bg_color']
    search_fields = list_display
    readonly_fields = ['slug']
