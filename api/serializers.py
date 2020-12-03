from rest_framework import serializers
from .models import Api


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Api
        fields = ('id', 'url', 'name', 'language', 'price')
