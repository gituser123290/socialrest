import pytest
from api.fixtures.user import user
from api.post.models import Post
@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user,body="Test Post Body")