
from django.contrib import admin
from django.urls import path,include
from p2 import views
from rest_framework.routers import DefaultRouter
from p2.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, token_obtain_pair, \
    token_refresh, token_verify

#create router
router=DefaultRouter()
#Register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='Student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),

]

