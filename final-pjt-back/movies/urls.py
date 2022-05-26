from django.urls import path
from . import views

# /

urlpatterns = [

    # Movie
    # 전체: 조회
    path('', views.movie_list),
    # Open API 호출 => Movie DB 저장
    path('movies/', views.movie_create),
    # 추천영화: 조회
    path('movies/recommendations/', views.movie_recommendations),
    # 단일: 조회
    path('movies/<int:movie_id>/', views.movie_detail),
    # 영화 평점: 등록/취소/수정
    path('movies/watched/<int:movie_id>/rate/', views.movie_rate),
]