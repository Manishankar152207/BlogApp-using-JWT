from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('my-blog/', views.MyBlogView.as_view(), name='myblog'),
    path('add-blog/', views.AddBlogView.as_view(), name='addblog'),
    path('blog-detail/<slug:the_slug>', views.BlogDetailView.as_view(), name='blogdetail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
