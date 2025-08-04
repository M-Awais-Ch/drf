# from http.client import HTTPResponse

from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Teacher
# from .serializer import TeacherSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
 # Create your views here.
# def  teacher_details(request):
#     teach=Teacher.objects.get(id=6)
#     serializer=TeacherSerializer(teach)
#     json_data=JSONRenderer().render(serializer.data)
#     return  HttpResponse(json_data,content_type='application/json')
@ csrf_exempt
def teacher_create(request):
    if request.method=='POST':
        json_data=request.body
        stream= io.BytesIO( json_data)
        pythondata= JSONParser().parse(stream)
        serializer=TeacherSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')




