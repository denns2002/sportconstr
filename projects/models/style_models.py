from django.db import models

from common.utils.slug_generator import SlugGeneratorMixin


class Palette(SlugGeneratorMixin):
    name = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255, null=True)
    secondary_color = models.CharField(max_length=255, null=True)
    bg_color = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name} ({self.main_color}, {self.secondary_color}, {self.bg_color})"


class Typography(SlugGeneratorMixin):
    name = models.CharField(max_length=255)
    font = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.font}"


class Style(SlugGeneratorMixin):
    typography = models.ForeignKey(Typography, null=True, blank=True, on_delete=models.SET_NULL)
    palette = models.ForeignKey(Palette, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.typography} {self.palette}"
