########## API for PageNumberPagination 
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    