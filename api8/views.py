#ModelViewSet 

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

from .serializers import StudentSerializer
from api.models import Student

# Create your views here.
class StudentAPI8(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentAPI8(ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer