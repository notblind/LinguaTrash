from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from accounts.serializers import UserSerializer


class UserAPI(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.get(pk=user.pk)

    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            serializer = self.get_serializer(self.get_queryset())
            return Response(serializer.data)
        return Response()
