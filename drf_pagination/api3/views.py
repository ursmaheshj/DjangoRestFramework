from rest_framework.viewsets import ModelViewSet

from api.models import Student
from api.serializers import StudentSerializer
from .pagination import MyCursorPagination

class StudentAPI3(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination