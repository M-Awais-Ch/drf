from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    dep = serializers.CharField(max_length=100)
    def create(self,validate_data):
        # if
        return Teacher.objects.create(**validate_data)

