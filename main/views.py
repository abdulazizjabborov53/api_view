from unicodedata import category

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import HeroSection, Category, Course
from .serializers import HeroSectionSerializer, CategorySerializer, CourseSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers
from .filters import CourseFilter


class Register(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')
        if password != password_confirm:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        data = {
            'message':',uvaffaq',
            'token': token.key,
        }
        return Response(data, status=status.HTTP_201_CREATED)

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        token,created = Token.objects.get_or_create(user=user)
        data = {
            'message':',uvaffaq',
            'token': token.key,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class JWTRegister(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')
        
        if password != password_confirm:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        
        data = {
            'message': 'Muvaffaqiyatli',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(data, status=status.HTTP_201_CREATED)


class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        data = {
            'message': 'Muvaffaqiyatli',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(data, status=status.HTTP_200_OK)


class JWTLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    def get(self, request, lang=None):
        hero = HeroSection.objects.last()
        hero_sr = HeroSectionSerializer(hero, context={'request': request, 'lang': lang})
        return Response(hero_sr.data)
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Course(APIView):
    def get(self,request):
        course = models.Course.objects.all()
        category=request.query_params.get('category')
        if category:
            course = course.filter(category_id=category)


        course_sr = serializers.CourseSerializer(course, many=True)
        data = {
            'courses': course_sr.data
        }
        return Response(data)

class CourseView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['name']
    ordering_fields = ['price', 'name']
    pagination_class = CustomPagination