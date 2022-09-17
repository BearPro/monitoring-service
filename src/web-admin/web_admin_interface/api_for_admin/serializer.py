from rest_framework import serializers

from .models import Users, Tokens

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['username']
    
class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tokens
        fields = ['id', 'owner', 'value_hash', 'name']
    