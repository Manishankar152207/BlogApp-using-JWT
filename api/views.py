from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import ExcludeAuthenticationForGetMethod
from rest_framework_simplejwt.authentication import JWTAuthentication

class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

