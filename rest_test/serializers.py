from django.contrib.auth.models import User, Group
from info.models import Information


from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class InformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Information
        fields = ('owner','title', 'description','pub_date',)