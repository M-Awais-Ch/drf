from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
class StudentConcrete(ListAPIView,RetrieveAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer





























# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.mixins import DestroyModelMixin
# #ham in sab ko alg alag class may b use kr sakty or pairing may kr sakty use
# class StudentCrud(GenericAPIView,ListModelMixin,RetrieveModelMixin,
#                   CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         # print('Data Posted Successfully')
#         return self.create(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
