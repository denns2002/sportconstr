from django.db import models

from projects.models.project_models import Module


class ProjectModuleMixin(models.Model):
    module = models.ForeignKey(Module, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
