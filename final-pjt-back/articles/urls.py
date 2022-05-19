from django.urls import path
from . import views

# community/

urlpatterns = [

    # Article
    # 전체: 조회, 단일: 생성
    path('', views.article_list_or_create),
    # 단일: 조회, 수정, 삭제
    path('<int:article_id>/', views.article_detail_or_update_or_delete),
    # 좋아요: 생성, 삭제
    path('<int:article_id>/like/', views.article_like_or_cancel),

    # Comment
    # 단일: 생성
    path('<int:article_id>/comment/', views.comment_create),
    # 단일: 수정, 삭제
    path('<int:article_id>/comment/<int:comment_id>/', views.comment_update_or_delete),
]