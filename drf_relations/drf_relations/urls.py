"""
URL configuration for drf_relations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from api.views import SingerAPI,SongAPI
from api2.views import SingerAPI2,SongAPI2
from api3.views import SingerAPI3,SongAPI3

router = DefaultRouter()
router.register('singerapi',SingerAPI)
router.register('songapi',SongAPI)
router.register('singerapi2',SingerAPI2)
router.register('songapi2',SongAPI2)
router.register('singerapi3',SingerAPI3)
router.register('songapi3',SongAPI3)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
