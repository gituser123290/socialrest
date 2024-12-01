from rest_framework import serializers
from api.user.serializers import UserSerializer
from api.user.models import User


class RegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation
    """
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ["id", "name","bio","avatar","email","username","first_name","last_name","password",]

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier for the UserManager to create a new user.
        return User.objects.create_user(**validated_data)
