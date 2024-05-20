from django.db import models

from common.utils.slug_generator import SlugGeneratorMixin


class CMS(SlugGeneratorMixin):
    CONTENT_TYPES = [
        ('char', 'char'),
        ('text', 'text'),
        ('image', 'image'),
        ('integer', "integer"),
        ('float', 'float'),
        ('datetime', 'datetime')
    ]

    content_type = models.CharField(max_length=15, choices=CONTENT_TYPES)
    title = models.CharField(max_length=255, blank=True, null=True)

    char = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'CMS'


class CMSMixin(SlugGeneratorMixin):
    cms = models.ForeignKey(CMS, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CMSChar(CMSMixin): pass
class CMSText(CMSMixin): pass
class CMSImage(CMSMixin): pass
class CMSInteger(CMSMixin): pass
class CMSFloat(CMSMixin): pass
class CMSDatetime(CMSMixin): pass

