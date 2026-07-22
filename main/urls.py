from lib2to3.pygram import pattern_grammar

from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('article-comments/<int:article_id>/', views.CommentListG.as_view(), name='comment-list'),
    path('article-comments/', views.ArticleCommentG.as_view(), name='article-comment-list'),
    path('articles/', views.ArticleListG.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetailG.as_view(), name='article-detail'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('jwt/register/', views.JWTRegister.as_view(), name='jwt_register'),
    path('jwt/login/', views.JWTLogin.as_view(), name='jwt_login'),
    path('jwt/logout/', views.JWTLogout.as_view(), name='jwt_logout'),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
