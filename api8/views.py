#ModelViewSet #ReadOnlyModelViewSet and #BasicAuthentication

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializer
from api.models import Student

# Create your views here.
class StudentAPI8(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
# class StudentAPI8(ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer