from rest_framework import serializers

from cms.models import *


class CMSSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        content_type = getattr(obj, obj.content_type)
        return content_type

    def validate(self, data):
        if sum(bool(x) for x in data.values()) > 3:
             raise serializers.ValidationError({"ERROR": "Many types"})

        return data

    class Meta:
        model = CMS
        fields = "__all__"
        read_only_fields = ['slug']


class CMSCharSerializer(serializers.ModelSerializer):
    cms = CMSSerializer()

    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSChar

    def create(self, validated_data):
        cms_data = validated_data.pop('cms')
        cms = CMS.objects.create(**cms_data)
        cms_type = self.Meta.model.objects.create(cms=cms)

        return cms_type


class CMSTextSerializer(CMSCharSerializer):
    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSText


class CMSImageSerializer(CMSCharSerializer):
    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSImage


class CMSIntegerSerializer(CMSCharSerializer):
    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSInteger


class CMSFloatSerializer(CMSCharSerializer):
    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSFloat


class CMSDatetimeSerializer(CMSCharSerializer):
    class Meta:
        fields = ['cms', 'slug']
        read_only_fields = ['slug']
        model = CMSDatetime
