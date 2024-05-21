from django.contrib.auth import get_user_model

from cms.models import *
from .groups import Group
from .mixins import ProjectModuleMixin


class Club(ProjectModuleMixin, SlugGeneratorMixin):
    name = models.ForeignKey(CMSChar, on_delete=models.CASCADE, related_name='club_name')
    info = models.ForeignKey(CMSText, on_delete=models.CASCADE, related_name='club_info')
    address = models.ForeignKey(CMSChar, on_delete=models.CASCADE, related_name='club_address')
    is_active = models.ForeignKey(CMSBool, on_delete=models.CASCADE, related_name='club_is_active')

    groups = models.ManyToManyField(Group, blank=True)
    managers = models.ManyToManyField(get_user_model(), blank=True)

    other_fields = models.ManyToManyField(CMS, blank=True, related_name='club_other_fields')
