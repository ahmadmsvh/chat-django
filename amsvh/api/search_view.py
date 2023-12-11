from rest_framework import generics
from usercomment.models import UserComment
from api.serializers import UserCommentSerializer


class SearchListView(generics.ListAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = UserComment.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results