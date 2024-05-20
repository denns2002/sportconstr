from django.db import models

from common.utils.slug_generator import SlugGeneratorMixin


class Typography(SlugGeneratorMixin):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255)
    secondary_color = models.CharField(max_length=255)
    bg_color = models.CharField(max_length=255)


class Palette(SlugGeneratorMixin):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255)
    font = models.FileField()


class Style(SlugGeneratorMixin):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    typography = models.ForeignKey(Typography, null=True, blank=True, on_delete=models.SET_NULL)
    palette = models.ForeignKey(Palette, null=True, blank=True, on_delete=models.SET_NULL)
