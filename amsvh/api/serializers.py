from rest_framework import serializers
from django.contrib.auth.models import User
from usercomment.models import UserComment
from .validators import validate_first_name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    inline = serializers.SerializerMethodField(read_only=True)

    def get_inline(self, obj):
        inline_qs = obj
        return UserInlineSerializer(inline_qs).data


class UserInlineSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)


class UserCommentSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='username', read_only=True)
    first_name = serializers.CharField(validators=[validate_first_name])
    class Meta:
        model = UserComment
        fields = [
            'owner',
            'id',
            'first_name',
            'last_name',
            'username',
            'comment',
            'public',
        ]


    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def validate_comment(self, value):
        if value == 'fuck you':
            raise serializers.ValidationError("this is not alowed to say fuck you!!!")
        return value
