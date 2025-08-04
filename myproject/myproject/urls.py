
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('teachinfo/', views.teacher_details),
    path('stucreate/', views.teacher_create),
]
