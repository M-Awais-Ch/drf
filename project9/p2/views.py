from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
class StudentModelViewSet(viewsets.ModelViewSet):
    print("hi")
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import viewsets
# class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     print("hi")
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer