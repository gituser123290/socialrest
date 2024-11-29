from django.urls import path,include
from rest_framework import routers
from api.user.views import UserViewSet
from api.auth.viewsets import RegisterViewSet,LoginViewSet, RefreshViewSet
from api.post.viewsets import PostViewSet



router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')

router.register('auth/register', RegisterViewSet,basename='auth-register')
router.register('auth/login', LoginViewSet,basename='auth-login')
router.register('auth/refresh', RefreshViewSet,basename='auth-refresh')

router.register('post', PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)), 
]