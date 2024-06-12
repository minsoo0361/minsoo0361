from rest_framework import serializers
from .models import Article, Comment, Choice


class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # ***** 필드 설정
        fields = ('title',)


class ArticleSerializer(serializers.ModelSerializer):
    # **** 게시글에 답글 갯수 카운트 필드 추가
    total_comment_count = serializers.IntegerField(
        source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # ***** 게시글 참조를 읽기 전용으로 설정 = 유효성 검사 제외!
        read_only_fields = ('article',)


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        ready_only_fields = ('article', 'comment',)
