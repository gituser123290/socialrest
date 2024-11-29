from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.abstract.serializers import AbstractSerializer
from api.user.serializers import UserSerializer
from api.post.models import Post
from api.user.models import User

class PostSerializer(AbstractSerializer):
    http_method_names = ('post', 'get', 'put', 'delete')
    
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value
    class Meta:
        model = Post
        # List of all the fields that can be included in a
        # request or a response
        fields = ['id', 'author', 'body', 'edited','created', 'updated']
        read_only_fields = ["edited"]
        
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance