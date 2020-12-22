from django.contrib import admin
from django.urls import path, include
from signupapi import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt import views as jwt_views
from signupapi.api import RegisterApi



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('router.urls')),
    
    # path('gettoken/', TokenObtainPairView.as_view(),name= 'token_obtain_pair'),
    # path('tokenrefresh/', TokenRefreshView.as_view(),name= 'token_refresh'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signupapi/', include('signupapi.urls')),



]