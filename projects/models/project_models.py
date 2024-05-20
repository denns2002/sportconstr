from django.contrib.auth import get_user_model
from django.db import models

from common.utils.slug_generator import SlugGeneratorMixin
from projects.models.style_models import Style


class Module(SlugGeneratorMixin):
    MODULES = [
        ('events', 'events'),
    ]

    name = models.CharField(max_length=255, choices=MODULES)
    description = models.TextField(blank=True, null=True)
    req_modules = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return str(self.name)


class Sample(SlugGeneratorMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    modules = models.ManyToManyField('Module', blank=True)

    def __str__(self):
        return str(self.name)


class Project(SlugGeneratorMixin):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    sample = models.ForeignKey(Sample, null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey(Style, null=True, blank=True, on_delete=models.SET_NULL)
    modules = models.ManyToManyField('Module')

    def __str__(self):
        return str(self.name)

