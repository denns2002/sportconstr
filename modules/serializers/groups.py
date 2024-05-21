from cms.serializers import *
from modules.models.groups import Group
from modules.serializers.mixins import CreateMixin
from users.serializers.user_serializer import UserSerializer


class GroupSerializer(CreateMixin, serializers.ModelSerializer):
    name = CMSCharSerializer()

    trainers = UserSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    other_fields = CMSSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'trainers', 'members', 'other_fields', 'slug')
        read_only_fields = ['slug']


class GroupTrainersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', "trainers", 'slug']


class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', "members", 'slug']
