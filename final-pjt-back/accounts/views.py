from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from movies.models import WatchedMovie, Movie
from .serializers.user import UserSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    serializer = UserSerializer(profile_user)
    return Response(serializer.data)    

@api_view(['POST'])
def follow(request, username):
    profile_user = get_object_or_404(User, username=username)
    request_user = get_object_or_404(User, id=request.user.id)
    
    if request_user != profile_user:
        if profile_user.followers.filter(id=request_user.id).exists():
            profile_user.followers.remove(request_user)
        else:
            profile_user.followers.add(request_user)

    serializer = UserSerializer(profile_user)
    return Response(serializer.data)

@api_view(['GET'])
def watched(request, username):
    # 평점 관련 기능 추가??
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)