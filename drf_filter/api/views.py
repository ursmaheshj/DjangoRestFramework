### Applying filter backend from django-filter

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

#Normal Filtering
# class StudentAPI(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         return Student.objects.filter(passby=self.request.user.id)


class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']