# GenericAPIView and Mixins

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response

from api.models import Student
from .serializers import StudentSerializer

# Create your views here.


# List and Create Mixin = pk required
class LCStudentAPI5(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    
# Retrieve, Update, Destroy mixin = pk not required    
class RUDStudentAPI5(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
