from django.db import models
from django.utils.timezone import now
# from django.db import models

class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f'{self.body}'
    class Meta:
        ordering = ['-created_at']

class Like(models.Model):
    post = models.ForeignKey(Post ,related_name = 'likes' ,on_delete=models.CASCADE)

class DisLike(models.Model):
    post = models.ForeignKey(Post ,related_name = 'dislikes' ,on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
