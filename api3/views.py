# Function based API View

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer
from api.models import Student

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api3(request,pk=None):
    try:
        if request.method == 'GET':
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
            
        if request.method == 'POST':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'student Created'})
            else:
                return Response(serializer.errors)
            
        if request.method == 'PUT':
            # id = request.data.get('id')
            id = pk
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Student Updated!!'})
            else:
                return Response(serializer.errors)
            
        if request.method == 'PATCH':
            # id = request.data.get('id')
            id = pk
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Student Updated!!'})
            else:
                return Response(serializer.errors)
            
        if request.method == 'DELETE':
            # id = request.data.get('id')
            id = pk
            try:
                stu = Student.objects.get(id=id)
                stu.delete()
                return Response({'msg':'Student deleted!'})
            except Exception:
                return Response({'msg':'Student not found'})

    except:    
        return Response({'msg':'Could not handle the request'})