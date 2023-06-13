# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if User.objects.filter(username = data['username']):
            raise serializers.ValidationError("Username already Exist.")

        if User.objects.filter(email = data['email']):
            raise serializers.ValidationError("Email already Exist.")

        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()