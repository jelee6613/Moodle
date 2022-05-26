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

class WatchedMovieSerializer(serializers.ModelSerializer):

    title = serializers.CharField(source='movie.title')
    genre = serializers.CharField(source='movie.genre')
    overview = serializers.CharField(source='movie.overview')
    poster_path = serializers.CharField(source='movie.poster_path')
    backdrop_path = serializers.CharField(source='movie.backdrop_path')
    director = serializers.CharField(source='movie.director')
    average_vote = serializers.FloatField(source='movie.average_vote')
    release_date = serializers.DateField(source='movie.release_date')
    
    class Meta:
        model = WatchedMovie
        fields = ('__all__')

class MovieValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path', 'backdrop_path', 'release_date',)
