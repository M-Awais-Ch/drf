from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def hellow_word(request):
    if request.method =='GET':
        return Response({'msg':'This Get message'})

    if request.method == 'POST':
        print(request.data)
    return Response({'msg':'This is post request','data':request.data})
