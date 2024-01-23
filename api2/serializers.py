# Modelserializer in Django
from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name']
