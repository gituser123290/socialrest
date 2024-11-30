import pytest
from api.fixtures.user import user
from api.fixtures.post import post
from api.comment.models import Comment
@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post,body="Test Comment Body")