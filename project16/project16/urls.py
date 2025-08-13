
from django.contrib import admin
from django.urls import path,include
from p2 import views
from rest_framework.routers import DefaultRouter

#create router
router=DefaultRouter()
#Register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='Student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),

]

