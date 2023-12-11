from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from .search_view import *


app_name = 'api'

urlpatterns = [
    path('auth/', obtain_auth_token),
    # path('auth/auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('guest/<int:pk>/', GuestMinxinView.as_view(), name='guestmixin'),
    path('guest/', GuestMinxinView.as_view(), name='guestmixin'),
    path('user/<int:pk>/', UserMinxinView.as_view(), name='usermixindetail'),
    path('user/', UserMinxinView.as_view(), name='usermixinlist'),
    path('usercomment/<int:pk>/', UserCommentMinxinView.as_view(), name='usercommentmixindetail'),
    path('usercomment/', UserCommentMinxinView.as_view(), name='usercommentmixinlist'),
    path('usercomment-search/', SearchListView.as_view(), name='searchlistview'),
    ]