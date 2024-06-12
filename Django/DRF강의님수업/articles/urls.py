from django.urls import path
from . import views

urlpatterns = [
    # 게시글들의 제목 필드만 조회해 가져오기
    path('articles/', views.get_article_titles, name='article-list'),

    # 답글 생성
    path('articles/<int:article_pk>/comments/',
         views.create_comment, name='comment-create'),

    # 게시글 상세 조회
    path('articles/<int:article_pk>/',
         views.get_article_detail, name='article-detail'),

    # 게시글 상세 조회에 기능 추가 (답글의 갯수 조회)
    path('articles/<int:article_pk>/detail/', views.get_article_detail_with_comment_count,
         name='article-detail-with-comment-count'),

    # 답글 삭제
    path('articles/<int:article_pk>/comments/<int:comment_pk>/',
         views.delete_comment, name='comment-delete'),

    # 답글에 좋아요 기능 추가
    path('articles/<int:article_pk>/comments/<int:comment_pk>/likes/',
         views.like_comment, name='like-create'),

    # 특정 게시글의 댓글만 조회하기
    path('articles/<int:article_pk>/comments/',
         views.get_article_comments, name='article-comments'),

    # 글 작성자의 채택 답글 생성 기능 추가
    path('comments/<int:comment_pk>/choice/',
         views.create_choice, name='choice-create'),

    # 글 작성자의 채택 답글 수정 기능 추가
    path('comments/<int:comment_pk>/choice/<int:choice_pk>/',
         views.update_choice, name='choice-update'),
]
