from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_id):
    pass

@api_view(['POST'])
def article_like_or_cancel(request, article_id):
    pass

@api_view(['POST'])
def comment_create(request, article_id):
    pass

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_id, comment_id):
    pass