import pytest
from api.fixtures.user import user
from api.fixtures.post import post
from api.comment.models import Comment
@pytest.mark.django_db
def test_create_comment(user, post):
    comment = Comment.objects.create(author=user, post=post,body="Test Comment Body")
    assert comment.author == user
    assert comment.post == post
    assert comment.body == "Test Comment Body"