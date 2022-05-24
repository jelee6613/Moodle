from django.forms import FloatField
from rest_framework import serializers
from ..models import Movie, WatchedMovie

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('__all__')

class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('__all__')

class MovieValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path', 'release_date',)


