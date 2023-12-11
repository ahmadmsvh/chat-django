from rest_framework import serializers

from .models import Guest

class GuestSerializer(serializers.ModelSerializer):
    identifier = serializers.SerializerMethodField(read_only=True)
    host = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Guest
        fields = [
            'identifier',
            'comment',
            'host',
        ]

    def get_identifier(self, obj):
        return obj.name()

    def get_host(self, obj):
        return "@amsvh.com"


class GuestSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = [
            'first_name',
            'last_name',
            'comment',
        ]