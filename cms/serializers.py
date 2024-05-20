from rest_framework import serializers

from cms.models import CMS


class CMSSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        content_type = getattr(obj, obj.content_type)
        return content_type

    def validate(self, data):
        if sum(bool(x) for x in data.values()) > 2:
             raise serializers.ValidationError({"ERROR": "Many types"})

        return data

    class Meta:
        model = CMS
        fields = "__all__"
        read_only_fields = ['slug']
