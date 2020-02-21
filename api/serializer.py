from rest_framework import serializers
from .models import Characters
from .models import Comics


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characters
        fields = ('name','url')

class ComicSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)
    class Meta:
        model = Comics
        fields = ('id','title','date','chapter','image','characters','url')

