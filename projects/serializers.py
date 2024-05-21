from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from modules.serializers.clubs import ClubSerializer
from projects.models.project_models import *
from projects.models.style_models import *


class SubModuleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Module
        fields = (
            'id',
            'name',
            'description',
            'is_active',
            'slug'
        )
        read_only_fields = ['slug']


class ModuleSerializer(SubModuleSerializer):
    class Meta:
        model = Module
        fields = (
            'id',
            'name',
            'description',
            'is_active',
            'project',
            'slug'
        )
        read_only_fields = ['slug']


class TypographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typography
        fields = (
            'id',
            'name',
            'font',
            'slug'
        )
        read_only_fields = ['slug']


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = (
            'id',
            'name',
            'main_color',
            'secondary_color',
            'bg_color',
            'slug'
        )
        read_only_fields = ['slug']


class SubSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'slug', 'name', 'description', 'image', 'modules')
        read_only_fields = ['slug']


class SampleSerializer(SubSampleSerializer):
    modules_names = SubModuleSerializer(many=True, source='modules', read_only=True)

    class Meta:
        model = Sample
        fields = ('id', 'slug', 'name', 'description', 'image', 'modules', 'modules_names')
        read_only_fields = ['slug']


class SubStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = (
            'id', 'slug', 'typography', 'palette'
        )
        read_only_fields = ['slug']


class StyleSerializer(serializers.ModelSerializer):
    typography_name = TypographySerializer(source='sample', read_only=True)
    palette_name = PaletteSerializer(source='style', read_only=True)

    class Meta:
        model = Style
        fields = (
            'id', 'slug', 'typography', 'palette',
            'typography_name', 'palette_name'
        )
        read_only_fields = ['slug']


class ProjectSerializer(serializers.ModelSerializer):
    sample_name = SubSampleSerializer(source='sample', read_only=True)
    style_name = SubStyleSerializer(source='style', read_only=True)
    module_set = SubModuleSerializer(many=True)

    def update(self, instance, validated_data):
        print(validated_data)
        for attr, value in validated_data.items():
            if attr == 'module_set':
                if attr:
                    qs = Module.objects.filter(project=instance)
                    for el in qs:
                        el.is_active = False
                        el.save()

                    for i in range(len(value)):
                        id = value[i].get('id')
                        if not id:
                            print(value[i])
                            m = Module.objects.create(**value[i])
                        else:
                            m = Module.objects.get(id=id)
                        m.is_active = True
                        m.project = instance
                        m.save()
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance

    class Meta:
        model = Project
        fields = [
            'id', 'user', 'slug', 'name', 'created_at',
            'sample', 'sample_name', 'style', 'style_name',
            'module_set'
        ]
        read_only_fields = ['slug', 'created_at']
