from rest_framework import viewsets
from usercomment.models import UserComment
from .serializers import UserCommentSerializer


class UserCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    lookup_field = 'pk'
