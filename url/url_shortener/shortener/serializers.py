from .models import ShortendURLModel
from rest_framework import serializers
class ShortendURLSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShortendURLModel
        fields="__all__"