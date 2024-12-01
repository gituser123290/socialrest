from django.db import models
from api.abstract.models import AbstractModel,AbstractManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class PostManager(AbstractManager):
    pass

class Post(AbstractModel):
    author = models.ForeignKey(to="api_user.User",on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = PostManager()
    def __str__(self):
        return f"{self.author.name}"