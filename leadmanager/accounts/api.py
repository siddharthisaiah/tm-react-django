from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer


# Register api
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user" : userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


# Login api


# Get user api
