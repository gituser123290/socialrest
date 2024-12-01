from django.db import models
from api.abstract.models import AbstractModel, AbstractManager
from django.utils.translation import gettext_lazy as _
class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    post = models.ForeignKey("api_post.Post",on_delete=models.PROTECT)
    author = models.ForeignKey("api_user.User",on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = CommentManager()
    
    def __str__(self):
        return self.author.name