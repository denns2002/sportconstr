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

        if not data.get(data['content_type']):
            raise serializers.ValidationError({"ERROR": "Incorrect type or content"})

        return data

    class Meta:
        model = CMS
        fields = (
            'id',
            'content',
            'content_type',
            'title',
            'char',
            'text',
            'image',
            'integer',
            'float',
            'datetime',
            'bool',
        )
        read_only_fields = ['slug']


class CMSTypeMixin(serializers.ModelSerializer):
    cms = CMSSerializer()

    def validate(self, data):
        cms_type = data['cms']['content_type']

        print(cms_type, self.Meta.cms_type)
        if cms_type != self.Meta.cms_type:
            raise serializers.ValidationError({"ERROR": "Incorrect type or content"})

        return data

    def create(self, validated_data):
        cms_data = validated_data.pop('cms')
        cms = CMS.objects.create(**cms_data)
        cms_type = self.Meta.model.objects.create(cms=cms)

        return cms_type


class CMSCharSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSChar
        cms_type = 'char'


class CMSTextSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSText
        cms_type = 'text'


class CMSImageSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSImage
        cms_type = 'image'


class CMSIntegerSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSInteger
        cms_type = 'integer'


class CMSFloatSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSFloat
        cms_type = 'float'


class CMSDatetimeSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSDatetime
        cms_type = 'datetime'


class CMSBoolSerializer(CMSTypeMixin):
    class Meta:
        fields = ['id', 'cms', 'slug']
        read_only_fields = ['slug']
        model = CMSDatetime
        cms_type = 'bool'
