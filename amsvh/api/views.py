from django.contrib.auth.models import User
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from guestcomment.serializers import GuestSerializerPost
from .serializers import UserSerializer, UserCommentSerializer
from guestcomment.models import Guest
from usercomment.models import UserComment
from .permissions import IsStaffPermission
from .sessions import handle_session
import subprocess
# from .authentication import TokentAuthentication
# from colors import Bcolors as C


class GuestMinxinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializerPost
    # permission_classes = [permissions.DjangoModelPermissions, ]
    permission_classes = []
    # authentication_classes = [authentication.SessionAuthentication]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        if kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if kwargs:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        bashCommand = "code"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        if kwargs:
            return self.destroy(request, *args, **kwargs)


class UserMinxinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions,]
    authentication_classes = [authentication.SessionAuthentication]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        if kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if kwargs:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if kwargs:
            return self.destroy(request, *args, **kwargs)

class UserCommentMinxinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    # permission_classes = [permissions.DjangoModelPermissions,]
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffPermission,
    ]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        # TokentAuthentication,
        # JWTAuthentication,
    ]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        if kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if kwargs:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if kwargs:
            return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return UserComment.objects.none()
        elif request.user.id == 2:
            return qs.filter(username=request.user)
        else:
            return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            response = handle_session(request, response)["response"]
            return response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)