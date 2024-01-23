"""
URL configuration for DRF project.

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
from django.urls import path
from api.views import studentAPI
from api2.views import studentAPI2
from api3.views import student_api3
from api4.views import StudentAPI4
from api5.views import LCStudentAPI5,RUDStudentAPI5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', studentAPI.as_view()),
    path('studentapi2/', studentAPI2.as_view()),
    path('studentapi3/',student_api3),
    path('studentapi3/<int:pk>',student_api3),
    path('studentapi4/',StudentAPI4.as_view()),
    path('studentapi4/<int:pk>',StudentAPI4.as_view()),
    path('studentapi5/',LCStudentAPI5.as_view()),
    path('studentapi5/<int:pk>',RUDStudentAPI5.as_view()),
    
]
