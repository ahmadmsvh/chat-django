from django.urls import path
from .views import UserCommentListView, UserCommentDetailView,\
    create, update, delete, handy, handy_chat, handy_delete, handy_create,\
    handy_json
from .views_picture import *
app_name = 'usercomment'

urlpatterns = [
    path('', UserCommentListView.as_view(), name='usercommentlist'),
    path('<int:pk>/detail/', UserCommentDetailView.as_view(), name='usercommentdetail'),
    path('create/', create, name='usercommentcreate'),
    path('update/', update, name='usercommentupdate'),
    path('<int:pk>/delete/', delete, name='usercommentdelete'),
    path('handy/', handy, name='handy'),
    path('handy-chat/', handy_chat, name='handy-chat'),
    path('<int:pk>/handy-delete/', handy_delete, name='handy-delete'),
    path('handy-create/', handy_create, name='handy-create'),
    path('handy/json/', handy_json, name='json'),

    path('picture/', PictureListView.as_view(), name='all'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='picture_detail'),
    path('picture/create/', PictureCreateView.as_view(success_url=reverse_lazy('usercomment:all')), name='picture_create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(success_url=reverse_lazy('usercomment:all')), name='picture_update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(success_url=reverse_lazy('usercomment:all')), name='picture_delete'),
    path('picture_picture/<int:pk>/', stream_file, name='picture_picture'),

]