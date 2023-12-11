from django.urls import path, include
from .views import *


app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sample-form/', SampleFormView.as_view(), name='sample-form'),
    ]