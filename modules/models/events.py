from django.contrib.auth import get_user_model

from cms.models import *
from .mixins import ProjectModuleMixin


class Event(ProjectModuleMixin, SlugGeneratorMixin):
    name = models.ForeignKey(CMSChar, on_delete=models.CASCADE, related_name='event_name')
    about = models.ForeignKey(CMSText, on_delete=models.CASCADE, related_name='event_about')
    address = models.ForeignKey(CMSChar, on_delete=models.CASCADE, related_name='event_address')
    is_attestation = models.ForeignKey(CMSBool, on_delete=models.CASCADE, related_name='event_is_attestation')
    is_seminar = models.ForeignKey(CMSBool, on_delete=models.CASCADE, related_name='event_is_seminar')
    reg_start = models.ForeignKey(CMSDatetime, null=True, on_delete=models.SET_NULL, related_name='event_reg_start')
    reg_end = models.ForeignKey(CMSDatetime, null=True, on_delete=models.SET_NULL, related_name='event_reg_end')
    date_start = models.ForeignKey(CMSDatetime, null=True, on_delete=models.SET_NULL, related_name='event_date_start')
    date_end = models.ForeignKey(CMSDatetime, null=True, on_delete=models.SET_NULL, related_name='event_date_end')

    members = models.ManyToManyField(get_user_model(), blank=True, related_name='event_members')
    organizers = models.ManyToManyField(get_user_model(), blank=True, related_name='event_organizers')
    other_fields = models.ManyToManyField(CMS, blank=True, related_name='event_other_fields')
