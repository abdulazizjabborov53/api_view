from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('home/<str:lang>/', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('jwt/register/', views.JWTRegister.as_view(), name='jwt_register'),
    path('jwt/login/', views.JWTLogin.as_view(), name='jwt_login'),
    path('jwt/logout/', views.JWTLogout.as_view(), name='jwt_logout'),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('courses/', views.CourseView.as_view(), name='courses'),
    path('course/', views.Course.as_view(), name='course'),
    path('category/', views.CategoryView.as_view(), name='category'),

]
