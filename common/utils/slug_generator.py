from django.db import models
from django.utils.crypto import get_random_string


class SlugGeneratorMixin(models.Model):
    """Rewrite save func for generate slug"""
    slug = models.SlugField(max_length=255, unique=True, null=True)

    @staticmethod
    def get_slug(model_class: models.Model):
        slug = get_random_string(length=10)

        while model_class.objects.filter(slug=slug).exists():
            slug = get_random_string(length=10)

        return slug

    def save(
            self, force_insert=False, force_update=False, using=None,
            update_fields=None
            ):
        if not self.slug:
            self.slug = self.get_slug(self.__class__)

        super().save()

    class Meta:
        abstract = True
