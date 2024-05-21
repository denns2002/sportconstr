from cms.serializers import *
from modules.models.news import News

from modules.serializers.mixins import CreateMixin


class NewsSerializer(CreateMixin, serializers.ModelSerializer):
    title = CMSCharSerializer()
    description = CMSTextSerializer()
    is_published = CMSBoolSerializer()

    other_fields = CMSSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'is_published', 'other_fields', 'slug')
        read_only_fields = ['slug']
