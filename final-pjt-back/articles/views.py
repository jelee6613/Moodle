from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def article_like_or_cancel(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
    serializer = CommentSerializer(article.comment_set, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method=='PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = CommentSerializer(article.comment_set, many=True)
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method=='DELETE':
        if request.user == comment.user:
            comment.delete()
            serializer = CommentSerializer(article.comment_set, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)