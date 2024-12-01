
from rest_framework_nested import routers
from api.post.viewsets import PostViewSet
from api.user.viewsets import UserViewSet
from api.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
# from .views import LogoutViewSet
from api.comment.viewsets import CommentViewSet

# Initialize the main router
router = routers.SimpleRouter()

# Register viewsets for authentication routes
router.register("auth/register", RegisterViewSet, basename="auth-register")
router.register("auth/login", LoginViewSet, basename="auth-login")
router.register("auth/refresh", RefreshViewSet, basename="auth-refresh")
# router.register("auth/logout", LogoutViewSet, basename="auth-logout")

# Register viewsets for user and post routes
router.register("user", UserViewSet, basename="user")
router.register("post", PostViewSet, basename="post")

# Initialize the nested router for comments under posts
posts_router = routers.NestedSimpleRouter(router, "post", lookup="post")
posts_router.register("comment", CommentViewSet, basename="post-comment")

# Combine the URL patterns
urlpatterns = [
    *router.urls,
    *posts_router.urls
]
