from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin
#ham in sab ko alg alag class may b use kr sakty or pairing may kr sakty use
class StudentCrud(GenericAPIView,ListModelMixin,RetrieveModelMixin,
                  CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        # print('Data Posted Successfully')
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)





















# from django.core.serializers import serialize
# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView
# # Create your views here.
# class StudentApi(APIView):
#     def get(self,request,pk=None,format=None):
#         id=pk
#         if id is not None:
#             # stu = Student.objects.filter(id=pk).first() or we cal use also below line
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'Data Created(POST)'})
#         return Response(serializer.errors)
#
#     def put(self,request,pk=None,format=None):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data is Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#     def patch(self,request,pk,format=None):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data is Updated'})
#         return Response(serializer.errors)
#
#     def delete(self,request,pk,format=None):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data is Deleted'})
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
