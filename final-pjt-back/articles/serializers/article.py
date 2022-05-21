from rest_framework import serializers
from ..models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('pk', 'username',)
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('__all__')



class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('pk', 'username',)
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('__all__')