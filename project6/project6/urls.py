from django.contrib import admin
from django.urls import path
from p2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentCrud.as_view()),
    path('studentapi/<int:pk>/',views.StudentCrud.as_view()),
]
