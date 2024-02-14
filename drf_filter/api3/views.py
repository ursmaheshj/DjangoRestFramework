### Applying Ordering Filter
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from api.models import Student
from api.serializers import StudentSerializer
# Create your views here.
class StudentAPI3(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','roll']