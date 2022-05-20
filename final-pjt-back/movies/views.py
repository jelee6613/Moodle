from django.shortcuts import render
from django.http import JsonResponse

import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def movie_list(request):
    pass
    
@api_view(['GET'])
def movie_detail(request):
    pass

@api_view(['GET'])
def movie_recommendations(request):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie_watched(request, username, movie_id):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie_rate(request, username, movie_id):
    pass