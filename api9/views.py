#SessionAuthentication #IsAuthenticatedOrReadOnly and #CustomPermissions

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from .serializers import StudentSerializer
from api.models import Student
from .custompermissions import MyPermission
from .customauthentication import MyAuthentication

class StudentAPI9(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [MyAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [IsAuthenticated]
