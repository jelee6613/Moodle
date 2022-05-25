from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from movies.serializers.movie import MovieDetailSerializer, MovieListSerializer
from articles.serializers.article import ArticleSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class UserFollowSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('pk', 'username')

    movies = MovieDetailSerializer(many=True, read_only=True)
    article_set = ArticleSerializer(many=True)
    followings = UserFollowSerializer(many=True)
    followers = UserFollowSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'movies', 'followings', 'followers', 'article_set', 'is_superuser',)

class WatchedMoviesSerializer(serializers.ModelSerializer):
    
    movie_id = MovieListSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('__all__')