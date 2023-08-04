from tokenize import TokenError

from jwt import InvalidTokenError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


# A custom view to return the access token without the refresh token
class SingleTokenView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as token_error:
            raise InvalidTokenError(token_error.args[0]) from token_error
        serializer.validated_data.pop('refresh', None)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
