from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    likes_count = models.IntegerField(default=0)


class Choice(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
