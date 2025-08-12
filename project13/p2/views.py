from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.decorators import (api_view,
authentication_classes,permission_classes)
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = request.data.get("id", None)
        #postman may data ko get krny k liay necht wali line replece kery gay oper wali line say
        #id = request.query_params.get("id", None)  # <-- yahan change
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Data Created(POST)'})
        return Response(serializer.errors)
    if request.method == 'PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is Updated'})
    if request.method =='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is Deleted'})



#Age may brwser may id likho to ya code hu ga


# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request, pk=None):
#     if request.method == 'GET':
#         if pk is not None:   # yahan pk use ho raha hai
#             stu = Student.objects.get(pk=pk)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'Data Created(POST)'})
#         return Response(serializer.errors)
#
#     if request.method == 'PUT':
#         stu = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data is Updated'})
#
#     if request.method =='DELETE':
#         stu = Student.objects.get(pk=pk)
#         stu.delete()
#         return Response({'msg': 'Data is Deleted'})




