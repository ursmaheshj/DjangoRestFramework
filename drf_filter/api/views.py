from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(passby=self.request.user.id)