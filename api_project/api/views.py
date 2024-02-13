from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import User, Company, Client
from .serializers import UserSerializer, CompanySerializer, ClientSerializer
# Create your views here.

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

