from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from api.models import Student
from api.serializers import StudentSerializer
# Create your views here.
class StudentAPI2(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name','=roll']