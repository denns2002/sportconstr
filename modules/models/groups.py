from django.contrib.auth import get_user_model

from cms.models import *
from .mixins import ProjectModuleMixin


class Group(ProjectModuleMixin, SlugGeneratorMixin):
    name = models.ForeignKey(CMSChar, on_delete=models.CASCADE, related_name='group_name')

    trainers = models.ManyToManyField(get_user_model(), blank=True, related_name='group_trainers')
    members = models.ManyToManyField(get_user_model(), blank=True, related_name='group_members')

    other_fields = models.ManyToManyField(CMS, blank=True, related_name='group_other_fields')
