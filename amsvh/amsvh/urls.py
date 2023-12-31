"""amsvh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView
from colors import Bcolors as C

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('home/', include('home.urls')),
    path('guestcomment/', include('guestcomment.urls')),
    path('usercomment/', include('usercomment.urls')),
    path('api/', include('api.urls')),
    path('api/v2/', include('amsvh.routers')),
]

try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')


# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# urlpatterns += [
#     re_path(r'^site/(?P<path>.*)$', serve,
#         {'document_root': os.path.join(BASE_DIR, 'site'),
#          'show_indexes': True},
#         name='site_path'
#         ),s
# ]

# Serve the favicon - Keep for later
# urlpatterns += [
#     path('favicon.ico', serve, {
#             'path': 'favicon.ico',
#             'document_root': os.path.join(BASE_DIR, '/static'),
#         }
#     ),
# ]