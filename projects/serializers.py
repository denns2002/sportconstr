from rest_framework import serializers

from projects.models.project_models import *
from projects.models.style_models import *


class SubModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ['slug']


class ModuleSerializer(SubModuleSerializer):
    modules = SubModuleSerializer(many=True, source='module', read_only=True)

    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ['slug']


class TypographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typography
        fields = "__all__"
        read_only_fields = ['slug']


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = "__all__"
        read_only_fields = ['slug']


class SubSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"
        read_only_fields = ['slug']


class SampleSerializer(SubSampleSerializer):
    modules_names = SubModuleSerializer(many=True, source='modules', read_only=True)

    class Meta:
        model = Sample
        fields = ('slug', 'name', 'description', 'image', 'modules', 'modules_names')
        read_only_fields = ['slug']


class SubStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"
        read_only_fields = ['slug']


class StyleSerializer(serializers.ModelSerializer):
    typography_name = SubSampleSerializer(source='sample', read_only=True)
    palette_name = SubStyleSerializer(source='style', read_only=True)

    class Meta:
        model = Style
        fields = (
            'slug', 'typography', 'palette',
            'typography_name', 'palette_name'
        )
        read_only_fields = ['slug']


class ProjectSerializer(serializers.ModelSerializer):
    sample_name = SubSampleSerializer(source='sample', read_only=True)
    style_name = SubStyleSerializer(source='style', read_only=True)
    modules_names = SubModuleSerializer(many=True, source='modules', read_only=True)

    class Meta:
        model = Project
        fields = [
            'user', 'slug', 'name', 'created_at',
            'sample', 'sample_name', 'style', 'style_name',
            'modules', 'modules_names'
        ]
        read_only_fields = ['slug', 'created_at']
