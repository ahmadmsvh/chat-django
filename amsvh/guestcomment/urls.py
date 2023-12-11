from django.urls import path
from .views import GuestListView, GuestDetailView, create, update, delete

app_name = 'guestcomment'

urlpatterns = [
    path('', GuestListView.as_view(), name='guestcommentlist'),
    path('<int:pk>/detail/', GuestDetailView.as_view(), name='guestcommentdetail'),
    path('create/', create, name='guestcommentcreate'),
    path('update/', update, name='guestcommentupdate'),
    path('<int:pk>/delete/', delete, name='guestcommentdelete'),

]