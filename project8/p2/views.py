from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    # def list(self,request):
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu, many=True)
    #     return Response(serializer.data)
    #
    def retrieve(self, request,pk):

        if pk is not None:

            # stu = Student.objects.filter(id=pk).first() or we cal use also below line
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self,request ):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Data Created(POST)'})
        return Response(serializer.errors)

    def update(self,request,pk):
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self,request,pk):
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Updated'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is Deleted'})







