from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from api.models import BlogPost, Category
from django.urls import resolve
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class IndexView(APIView):
    def get(self, request):
        posts = BlogPost.objects.all()
        return render(request, 'index.html', context={'posts':posts, 'current_path':resolve(request.path).url_name})

class MyBlogView(APIView):
    def delete(self, request, pk, format=None):        
        posts = BlogPost.objects.filter(author=request.user)
        return render(request, 'index.html', context={'posts':posts, 'current_path':resolve(request.path).url_name})
    
    def get(self, request):
        posts = BlogPost.objects.filter(author=request.user)
        return render(request, 'index.html', context={'posts':posts, 'current_path':resolve(request.path).url_name})

class AddBlogView(APIView):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'addblog.html', context={'category': category, 'current_path':resolve(request.path).url_name})

class EditBlogView(APIView):
    def get(self, request, pk, format=None):
        post = BlogPost.objects.filter(id=pk).exists()
        if post:
            post = BlogPost.objects.filter(id=pk).first()
            category = Category.objects.all()
            return render(request, 'editblog.html', context={'post':post, 'category': category, 'current_path':resolve(request.path).url_name})
        else:
            return render(request, 'page_404.html')

class BlogDetailView(APIView):
    def get(self, request, the_slug, format=None):
        post = BlogPost.objects.filter(slug=the_slug).exists()
        if post:
            post = BlogPost.objects.filter(slug=the_slug).first()
            posts = BlogPost.objects.all()
            return render(request, 'blogdetail.html', context={'posts':posts, 'post':post, 'current_path':resolve(request.path).url_name})
        else:
            return render(request, 'page_404.html')

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            messages.success(request, "Registration successful. You can login now." )
            return Response({"success":True}, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        return render(request, 'register.html', context={'current_path':resolve(request.path).url_name})
    
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                refresh = RefreshToken.for_user(user)
                messages.success(request, "You are logged in successfully." )
                response = Response()
                response.data = {'success': True, 'access_token': str(refresh.access_token), 'refresh_token':str(refresh)}
                return response
            else:
                return Response({'success': False, 'error': 'Invalid credentials.'}, status=401)
        else:
            return Response(serializer.errors, status=400)
    
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'login.html', context={'current_path':resolve(request.path).url_name})
        return redirect('blog:home')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.") 

    return redirect('blog:login')
        