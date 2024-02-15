from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.
class StudentAPI2(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # pagination_class = LimitOffsetPagination
