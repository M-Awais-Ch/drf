
from django.contrib import admin
from django.urls import path
from p2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.hellow_word),
]
