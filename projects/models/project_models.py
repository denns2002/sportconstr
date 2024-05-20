from django.db import models

from common.utils.slug_generator import SlugGeneratorMixin
from projects.models.style_models import Style


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Sample(SlugGeneratorMixin):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)


class Module(models.Model):
    name = models.CharField(max_length=255)
    req_modules = models.ManyToManyField('self')


class Project(SlugGeneratorMixin):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    sample = models.ForeignKey(Sample, null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey(Style, null=True, blank=True, on_delete=models.SET_NULL)
    modules = models.ManyToManyField(Module)

