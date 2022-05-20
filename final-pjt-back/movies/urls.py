from django.urls import path
from . import views

# /

urlpatterns = [

    # Movie
    # 전체: 조회, 단일: 생성
    path('', views.movie_list),
    # 단일: 조회, 수정, 삭제
    path('movies/<int:movie_id>/', views.movie_detail),
    # 추천영화: 조회
    path('movies/recommendations/', views.movie_recommendations),
    # 내가 본 영화: 생성, 조회, 수정, 삭제
    path('movies/<str:username>/watched/<int:movie_id>/', views.movie_watched),
    # 영화 평점: 생성, 조회, 수정, 삭제
    path('movies/<str:username>/watched/<int:movie_id>/rate/', views.movie_rate),

]
