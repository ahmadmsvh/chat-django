from rest_framework import serializers
from colors import Bcolors as C


def validate_first_name(value):
    if value == "fuck":
        raise serializers.ValidationError(f"{value} is not allowed name!!!")
    return value