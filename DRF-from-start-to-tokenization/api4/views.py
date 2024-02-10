# Class Based APIView

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPI4(APIView):
    def get(self,request,pk=None,format=None):
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)
           
            
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'student Created'})
        else:
            return Response(serializer.errors)
            
    def put(self,request,pk,format=None):
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student Updated!!'})
        else:
            return Response(serializer.errors)
            
    def patch(self,request,pk,format=None):
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student Updated!!'})
        else:
            return Response(serializer.errors)
            
    def delete(self,request,pk,format=None):
        # id = request.data.get('id')
        id = pk
        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg':'Student deleted!'})
        except Exception:
            return Response({'msg':'Student not found'})

    