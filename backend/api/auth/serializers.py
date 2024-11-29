from rest_framework import serializers
from api.user.serializers import UserSerializer
from api.user.models import User

class RegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation
    """
    #Making sure the password is at least 8 characters long, and no longer than 128 and can't be read by the user
    password = serializers.CharField(max_length=128,min_length=8, write_only=True, required=True)
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'bio', 'avatar', 'email','username', 'first_name', 'last_name','password']
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
        

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from api.user.serializers import UserSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data