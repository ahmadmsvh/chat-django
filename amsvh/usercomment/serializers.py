from rest_framework import serializers

from .models import UserComment



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = [
            'first_name',
            'last_name',
            'username',
            'comment',
        ]