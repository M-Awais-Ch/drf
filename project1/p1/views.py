from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def student_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from .serializer import StudentSerializer
# from .models import Student
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
#
#
# # Create your views here.
# @csrf_exempt
# def student_api(request, id=None):
#     if request.method == 'GET':
#         # json_data=request.body
#         # stream=io.BytesIO(json_data)
#         # pythondata=JSONParser().parse(stream)
#         # print(pythondata)
#         # id=pythondata.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#         res = {'msg': 'Data Created'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#     # json_data = JSONRenderer().render(serializer.errors)
#     # return HttpResponse(json_data, con_
#
# #     if request.method == 'PUT':
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         pythondata = JSONParser().parse(stream)
# #         id = pythondata.get('id')
# #         stu = Student.objects.get(id=id)
# #         serializer = StudentSerializer(stu, data=pythondata, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #     res = {'msg': 'Data Updated'}
# #     json_data = JSONRenderer().render(res)
# #     return HttpResponse(json_data, content_type='application/json')
# # # json_data = JSONRenderer().render(serializer.errors)
# # # return HttpResponse(json_data, content_type='application/json')
