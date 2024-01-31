#Concrete view Classes
#ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
#ListCreateAPIView,RetrieveUpdateDestroyAPIView

from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from api.models import Student
from .serializers import StudentSerializer

# Create your views here.
class LCStudentAPI6(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUDStudentAPI6(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
