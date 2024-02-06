from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializer
from api.models import Student

class StudentAPI10(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]