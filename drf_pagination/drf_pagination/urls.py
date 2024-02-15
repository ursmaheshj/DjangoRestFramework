"""
URL configuration for drf_pagination project.

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

from api.views import StudentAPI
from api2.views import StudentAPI2
from api3.views import StudentAPI3

router = DefaultRouter()
router.register('studentapi',StudentAPI)
router.register('studentapi2',StudentAPI2)
router.register('studentapi3',StudentAPI3)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
