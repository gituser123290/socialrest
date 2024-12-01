from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from api.abstract.viewsets import AbstractViewSet
from api.post.models import Post
from api.post.serializers import PostSerializer
from api.auth.permissions import UserPermission


class PostViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (UserPermission,)
    serializer_class = PostSerializer
    filterset_fields = ["author__public_id"]

    def get_queryset(self):
        return Post.objects.all()

    def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        # Directly assigning the queryset to post_objects
        post_objects = self.filter_queryset(self.get_queryset())  # No need to check if it's None
        
        # Paginate the queryset if needed
        page = self.paginate_queryset(post_objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If pagination is not used, serialize the full queryset
        serializer = self.get_serializer(post_objects, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail=True)
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user

        # User likes the post
        user.like_post(post)

        serializer = self.serializer_class(post, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user

        # User removes the like on the post
        user.remove_like_post(post)

        serializer = self.serializer_class(post, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
