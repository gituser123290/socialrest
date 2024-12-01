from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from api.auth.permissions import UserPermission 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView

class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (UserPermission,)
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        refresh = request.data.get("refresh")
        if refresh is None:
            raise ValidationError({"detail": "A refresh token is required."})

        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({"detail": "The refresh token is invalid."})

