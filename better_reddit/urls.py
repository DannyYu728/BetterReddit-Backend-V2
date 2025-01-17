"""better_reddit URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from breddit.views import LikedPostView, FavoriteView, ChangePasswordView, UnLikedPostView

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(('breddit.routers', 'breddit'), namespace='breddit-api')),
    path('api/unlikePost/', UnLikedPostView.as_view()),
    path('api/likePost/', LikedPostView.as_view()),
    path('api/favorite/', FavoriteView.as_view()),
    path('api/auth/changePw/', ChangePasswordView.as_view(), name='changePw'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

