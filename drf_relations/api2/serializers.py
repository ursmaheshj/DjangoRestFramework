########### HyperlinkedModelSerializer Serializer ##########

from rest_framework import serializers
from api.models import Singer,Song

class SingerSerializer(serializers.HyperlinkedModelSerializer):
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model = Singer
        fields = '__all__'

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
