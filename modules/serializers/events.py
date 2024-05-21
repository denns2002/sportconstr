from cms.serializers import *
from modules.models.events import Event
from modules.serializers.mixins import CreateMixin
from users.serializers.user_serializer import UserSerializer


class EventSerializer(CreateMixin, serializers.ModelSerializer):
    name = CMSCharSerializer()
    about = CMSTextSerializer()
    address = CMSCharSerializer()
    is_attestation = CMSBoolSerializer()
    is_seminar = CMSBoolSerializer()
    reg_start = CMSDatetimeSerializer()
    reg_end = CMSDatetimeSerializer()
    date_start = CMSDatetimeSerializer()
    date_end = CMSDatetimeSerializer()
    other_fields = CMSSerializer(many=True)

    members = UserSerializer(many=True, read_only=True)
    organizers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'about',
            'address',
            'is_attestation',
            'is_seminar',
            'reg_start',
            'reg_end',
            'date_start',
            'date_end',
            'other_fields',
            'members',
            'organizers',
            'slug'
        )
        read_only_fields = ['slug']


class EventOrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', "organizers", 'slug']


class EventUpdatersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', "members", 'slug']
