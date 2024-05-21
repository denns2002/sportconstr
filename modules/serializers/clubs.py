from cms.serializers import *
from modules.models.clubs import Club
from modules.serializers.groups import GroupSerializer
from modules.serializers.mixins import CreateMixin
from users.serializers.user_serializer import UserSerializer


class ClubSerializer(CreateMixin, serializers.ModelSerializer):
    name = CMSCharSerializer()
    info = CMSTextSerializer()
    address = CMSCharSerializer()
    is_active = CMSBoolSerializer()

    groups = GroupSerializer(many=True, read_only=True)
    managers = UserSerializer(many=True, read_only=True)

    other_fields = CMSSerializer(many=True)

    class Meta:
        model = Club
        fields = ('id', 'name', 'info', 'address', 'is_active',
                  'groups', 'managers', 'other_fields')
        read_only_fields = ['slug']


class ClubGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', "groups"]


class ClubManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', "managers"]
