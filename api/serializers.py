from rest_framework import serializers
from .models import Student

def start_with_R(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name Should be start with R')


#serializer with serializer class from scratch
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  
    name = serializers.CharField(max_length=100,validators=[start_with_R])    
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'krishna' and ct.lower() != 'dwarka':
            raise serializers.ValidationError('City must be dwarka')
        return data
