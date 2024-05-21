from cms.serializers import *


class CreateMixin(metaclass=serializers.SerializerMetaclass):
    def create(self, validated_data):
        types = {
            'char': CMSChar,
            'text': CMSText,
            'integer': CMSInteger,
            'float': CMSFloat,
            'bool': CMSBool,
            'image': CMSImage,
            'datetime': CMSDatetime
        }

        if 'other_fields' in validated_data:
            other_fields = validated_data.pop('other_fields')

        for k, v in validated_data.items():
            if isinstance(v, dict):
                content_type = v['cms']['content_type']
                cms = CMS.objects.create(**v['cms'])
                content = types[content_type].objects.create(cms=cms)
                validated_data[k] = content

        instance = self.Meta.model.objects.create(**validated_data)

        if other_fields:
            for content in other_fields:
                cms = CMS.objects.create(**content)
                instance.other_fields.add(cms)

        return instance

