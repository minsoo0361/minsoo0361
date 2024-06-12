from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment, Choice
from .serializers import ArticleSerializer, ArticleTitleSerializer, CommentSerializer, ChoiceSerializer


# 게시글들의 제목 필드만 조회해 가져오기
@api_view(['GET'])
def get_article_titles(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article)
    serializer = ArticleTitleSerializer(articles, many=True)
    return Response(serializer.data)

# 답글 생성


@api_view(['POST'])
def create_comment(request, article_pk):
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 게시글 상세 조회
@api_view(['GET'])
def get_article_detail(request, article_pk):
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    article = get_object_or_404(Article, pk=article_pk)

    serializer = ArticleSerializer(article)

    # + 게시글 상세 조회에 기능 추가 (답글의 갯수 조회)
    return Response(serializer.data)


# 답글 삭제 메시지 및 상태코드 값을 적절히 수정해보기
@api_view(['DELETE'])
def delete_comment(request, article_pk, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk, article_id=article_pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    # return Response(serializer.data)
    return Response({'message': f'{comment_pk}번 댓글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

# 답글에 좋아요 기능 추가
@api_view(['POST'])
def like_comment(request, article_pk, comment_pk):
    # 답글을 조회해서 likes_count 값을 1 증가시키기
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.likes_count += 1
    comment.save()
    # 좋아요 기능 구현
    return Response(comment, status=status.HTTP_200_OK)

# 특정 게시글의 댓글만 조회하기


@api_view(['GET'])
def get_article_comments(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comments = article.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 글 작성자의 채택 답글 생성 기능 추가


@api_view(['POST'])
def create_choice(request, comment_pk):
    # 채택 답글 생성 기능 구현
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = comment.article
    # 사용자의 입력 데이터를 먼저 유효성 검사를 수행한다...
    serializer = ChoiceSerializer(data=request.data)
    # 그 후에 comment와 article에 대한 외래키 연결을 수행하여 저장한다.!
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)

# 글 작성자의 채택 답글 수정 기능 추가


@api_view(['PUT'])
def update_choice(request, comment_pk, choice_pk):
    # 채택 답글 수정 기능 구현 (*일부분만 수정할 수 있도록 하겠다!)
    choice = get_object_or_404(Choice, pk=choice_pk)
    serializer = ChoiceSerializer(choice, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)
