from django.shortcuts import render
from .models import Users, Tokens
from rest_framework import generics
from .serializer import UserSerializer, TokenSerializer


class UserList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class TokenList(generics.ListAPIView):
    queryset = Tokens.objects.all()
    serializer_class = TokenSerializer