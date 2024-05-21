from django.contrib.auth import get_user_model

from cms.models import *
from .mixins import ProjectModuleMixin


class News(ProjectModuleMixin, SlugGeneratorMixin):
    title = models.ForeignKey(CMSChar, on_delete=models.CASCADE)
    description = models.ForeignKey(CMSText, on_delete=models.CASCADE)
    is_published = models.ForeignKey(CMSBool, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

    other_fields = models.ManyToManyField(CMS, blank=True)


