########## API for PageNumberPagination 
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer
from .pagination import MyPageNumberPagination

# Create your views here.
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
