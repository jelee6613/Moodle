from rest_framework import serializers
from traitlets import default
from ..models import Movie

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
        fields = ('title', 'overview', 'poster_path', 'backdrop_path', 'release_date',)


