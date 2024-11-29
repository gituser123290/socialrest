from django.db import models
from api.abstract.models import AbstractModel,AbstractManager

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
    class Meta:
        db_table = 'api.post'