from rest_framework.routers import DefaultRouter
from api.viewsets import UserCommentViewSet


router = DefaultRouter()
router.register('usercommentset', UserCommentViewSet, basename='usercomment')

urlpatterns = router.urls
