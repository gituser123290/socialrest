from django.urls import path,include
from rest_framework import routers
from rest_framework_nested import routers
from api.user.views import UserViewSet
from api.auth.viewsets import RegisterViewSet,LoginViewSet, RefreshViewSet
from api.post.viewsets import PostViewSet
from api.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()
router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')

router.register('auth/register', RegisterViewSet,basename='auth-register')
router.register('auth/login', LoginViewSet,basename='auth-login')
router.register('auth/refresh', RefreshViewSet,basename='auth-refresh')

router.register('post', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router,'post', lookup='post')
posts_router.register('comment', CommentViewSet,basename='post-comment')


urlpatterns = [
    # path('', include(router.urls)), 
    *router.urls,
    *posts_router.urls
]