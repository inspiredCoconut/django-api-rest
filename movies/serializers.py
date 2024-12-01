from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for movie model
    
    Fields:
        - id: IntegerField
        - title: CharField
        - genre: CharField
        - year: IntegerField
        - creator: ReadOnlyField
        
    """
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model
    
    Fields:
        - id: IntegerField
        - username: CharField
        - movies: PrimaryKeyRelatedField
        
    """
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
